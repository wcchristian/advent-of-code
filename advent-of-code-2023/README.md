# Advent of Code YYYY

[![Java CI with Gradle](https://github.com/wcchristian/advent-of-code-2022/actions/workflows/gradle.yml/badge.svg)](https://github.com/wcchristian/advent-of-code-2022/actions/workflows/gradle.yml)

This repo houses my solutions for Advent of Code YYYY

https://adventofcode.com/

# Running The Solutions
You can run the solutions with `./gradlew run`. This will print out all of the solutions.

You can also check them for accuracy by using `./gradlew test`.

# Workflow
Each Day...
1. Copy the input and example input into the resources directory
2. Duplicate Day00.kt in the puzzle package and name it according to the day of the puzzle (Day00 is a template file)

NOTE: The FileLoader handles a few types automatically but depending on the input for the puzzle you may have to add cases to the
when statement.

# Versions
Java 17
Gradle 7.5.1
Kotlin 1.7.20
