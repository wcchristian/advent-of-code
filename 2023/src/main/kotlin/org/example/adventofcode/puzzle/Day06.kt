package org.example.adventofcode.puzzle

import org.example.adventofcode.util.Utils

object Day06 {
    fun part1(filePath: String): Long {
        val fileLines = Utils.loadFromFile<String>(filePath)
        return parseRaces(fileLines).map {
            findWaysToWin(it.first, it.second)
        }.reduce { acc, numWaysToWin -> acc * numWaysToWin }
    }

    fun part2(filePath: String): Long {
        val fileLines = Utils.loadFromFile<String>(filePath)
        val (time, distance) = parsePart2(fileLines)
        return findWaysToWin(time, distance)
    }

    private fun findWaysToWin(time: Long, recordDistance: Long): Long {
        return (0..time).count { buttonHeldTime ->
            (time - buttonHeldTime) * buttonHeldTime > recordDistance
        }.toLong()
    }

    private fun parseRaces(fileLines: List<String>): List<Pair<Long, Long>> {
        val findDigitsRegex = Regex("(\\d+)")
        val times = findDigitsRegex.findAll(fileLines[0]).map { it.value.toLong() }.toList()
        val distances = findDigitsRegex.findAll(fileLines[1]).map { it.value.toLong() }.toList()

        // Not sure why but toMap here takes 4 Pairs from the zip and gives me a map with only 3 keys? Instead I'll just use
        // the pairs that come from zip
        return times.zip(distances)
    }

    private fun parsePart2(fileLines: List<String>): Pair<Long, Long> {
        val time = fileLines[0].split(":")[1].trim().replace(" ", "").toLong()
        val distance = fileLines[1].split(":")[1].trim().replace(" ", "").toLong()
        return Pair(time, distance)
    }
}

fun main() {
    println("Part 1 example solution is: ${Day06.part1("/day06_example.txt")}")
    println("Part 1 main solution is: ${Day06.part1("/day06.txt")}")
    println("Part 2 example solution is: ${Day06.part2("/day06_example.txt")}")
    println("Part 2 main solution is: ${Day06.part2("/day06.txt")}")
}