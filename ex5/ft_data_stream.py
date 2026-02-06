import sys


time = sys.modules.get('time')


def lcg_generator():
    """Generates random numbers without using any imports.

    Yields:
        A random integer.
    """
    m = 2**31
    a = 1103515245
    c = 12345

    current = (time.time() * 1000).__int__()
    while True:
        current = (a * current + c) % m
        yield current


def lol_event_generator():
    """Generates a stream of mock game events.

    Args:
        count: The total number of events to generate.

    Yields:
        A random player with random level and random event.
    """
    lsc_gen = lcg_generator()
    lol_events = [
        "First Blood", "Kill" "Double Kill", "Triple Kill", "Quadra Kill",
        "Penta Kill", "Hexakill", "Ace", "Executed", "Shut Down",
        "Killing Spree", "Rampage", "Unstoppable", "Dominating", "Godlike",
        "Legendary", "Turret Destroyed", "Inhibitor Destroyed",
        "Inhibitor Respawning Soon", "Inhibitor Has Respawned",
        "Nexus Under Attack", "Dragon Slain", "Baron Nashor Slain",
        "Rift Herald Slain", "Victory", "Defeat"
    ]
    players = ["Chaos", "Spasha", "Darius"]

    while True:
        e_index = next(lsc_gen) % len(lol_events)
        p_index = next(lsc_gen) % len(players)

        yield players[p_index], next(lsc_gen) % 18, lol_events[e_index]


def fibonacci_gen(limit: int):
    """
    Generates a sequence of Fibonacci numbers.

    Args:
        limit: The number of Fibonacci elements to produce.

    Yields:
        The next number in the Fibonacci sequence.
    """
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b


def prime_gen(limit: int):
    """Generates a sequence of prime numbers.

    Args:
        limit: The number of prime numbers to produce.

    Yields:
        The next prime number.
    """

    count = 0
    num = 2

    def is_prime() -> bool:
        for i in range(2, int(num**0.5) + 1):
            if not num % i:
                return False
        return True

    while count < limit:
        if is_prime():
            count += 1
            yield num
        num += 1


def proces_lol_events(event_num):

    print(f"Processing {event_num} league of legends game events...")

    lol_gen = lol_event_generator()
    counter = {
        "High-level": 0,
        "Kill": 0,
        "Destroyed": 0
    }
    start = time.time()

    for i in range(1, event_num + 1):
        player, level, event = next(lol_gen)

        if level > 10:
            counter['High-level'] += 1
        elif "Kill" in event:
            counter['Kill'] += 1
        elif "Destroyed" in event:
            counter['Destroyed'] += 1

        print(f"Event {i}: Player {player} (level {level}) {event}")

    end = time.time()

    print("=== Stream Analytics ===")
    print(f"Total events processed: {event_num}")
    print(f"High-level players (+10): {counter['High-level']}")
    print(f"Kill events: {counter['Kill']}")
    print(f"Destroyed events: {counter['Destroyed']}")
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: ({(end - start):.3f}) seconds")


def main():

    print("=== Game Data Stream Processor ===\n")

    proces_lol_events(1000)

    print("=== Generator Demonstration ===")
    fib_list = [n.__str__() for n in fibonacci_gen(10)]
    print("Fibonacci sequence (first 10):", ', '.join(fib_list))

    prime_list = [n.__str__() for n in prime_gen(5)]
    print("Prime numbers (first 5):", ', '.join(prime_list))


if __name__ == "__main__":
    main()
