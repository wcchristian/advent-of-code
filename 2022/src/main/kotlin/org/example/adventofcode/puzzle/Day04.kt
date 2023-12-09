package org.example.adventofcode.puzzle

import org.example.adventofcode.util.FileLoader

object Day04 {
    fun part1(filePath: String): Int {
        val lines = FileLoader.loadFromFile<String>(filePath)
        var numContains = 0
        for (line in lines) {
            val groupPart = line.split(",")
            val ranges = ArrayList<Range>()
            for (part in groupPart) {
                val rangePart = part.split("-")
                ranges.add(Range(rangePart[0].toInt(), rangePart[1].toInt()))
            }

            if (ranges[0].min >= ranges[1].min && ranges[0].max <= ranges[1].max
                || ranges[1].min >= ranges[0].min && ranges[1].max <= ranges[0].max) {
                numContains += 1
            }
        }
        return numContains
    }

    fun part2(filePath: String): Int {
        val lines = FileLoader.loadFromFile<String>(filePath)
        var numContains = 0
        for (line in lines) {
            val groupPart = line.split(",")
            val ranges = ArrayList<Range>()
            for (part in groupPart) {
                val rangePart = part.split("-")
                ranges.add(Range(rangePart[0].toInt(), rangePart[1].toInt()))
            }

            if((ranges[0].min >= ranges[1].min && ranges[0].min <= ranges[1].max)
                || ranges[1].min >= ranges[0].min && ranges[1].min <= ranges[0].max
                || ranges[0].max <= ranges[1].max && ranges[0].max >= ranges[1].min
                || ranges[1].max <= ranges[0].max && ranges[1].max >= ranges[0].min) {
                numContains += 1
            }
        }
        return numContains
    }
}

data class Range(
    val min: Int,
    val max: Int
)

fun main() {
    println("Part 1 example solution is: ${Day04.part1("/day04_example.txt")}")
    println("Part 1 main solution is: ${Day04.part1("/day04.txt")}")
    println("Part 2 example solution is: ${Day04.part2("/day04_example.txt")}")
    println("Part 2 main solution is: ${Day04.part2("/day04.txt")}")
}