"""make.fun 'Six Words, One Story' entry: writes the story to /output/entry.txt."""
import os

STORY = "Still walk at six. Leash empty."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
