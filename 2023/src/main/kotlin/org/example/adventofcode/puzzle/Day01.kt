package org.example.adventofcode.puzzle

import org.example.adventofcode.util.FileLoader

val numberMap = mapOf(
    "one"   to "1",
    "two"   to "2",
    "three" to "3",
    "four"  to "4",
    "five"  to "5",
    "six"   to "6",
    "seven" to "7",
    "eight" to "8",
    "nine"  to "9"
)

object Day01 {
    fun part1(filePath: String): Int {
        val fileLines = FileLoader.loadFromFile<String>(filePath)
        return fileLines.sumOf {
            val matchIterator = Regex("(\\d)").findAll(it.lowercase())
            (matchIterator.first().groupValues[0] + matchIterator.last().groupValues[0]).toInt()
        }
    }

    // Lessons learned in part 2. I had the solution working for the most part but ended up getting stuck.
    // Kotlins findAll doesn't handle overlapping tokens like threeight. It finds the three and finds nothing from ight that is left over.
    // Part 1 was my original solution that I tried to use for part 2 (expanding the regexp pattern to what I have on the firstMatch line below)
    // Took quite a bit of time to get this figured out, oof. Fun first day.
    // ¯\_(ツ)_/¯
    fun part2(filePath: String): Int {
        val fileLines = FileLoader.loadFromFile<String>(filePath)
        return fileLines.sumOf {
            val firstMatch = Regex("(\\d|one|two|three|four|five|six|seven|eight|nine)").find(it.lowercase())!!
            val lastMatch = Regex("(\\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)").find(it.lowercase().reversed())!!
            val firstDigit = if(firstMatch.value.toIntOrNull() == null) numberMap[firstMatch.value] else firstMatch.value
            val lastDigit = if(lastMatch.value.toIntOrNull() == null) numberMap[lastMatch.value.reversed()] else lastMatch.value
            (firstDigit + lastDigit).toInt()
        }
    }
}

fun main() {
    println("Part 1 example solution is: ${Day01.part1("/day01_example.txt")}")
    println("Part 1 main solution is: ${Day01.part1("/day01.txt")}")
    println("Part 2 example solution is: ${Day01.part2("/day01p2_example.txt")}")
    println("Part 2 main solution is: ${Day01.part2("/day01.txt")}")
}