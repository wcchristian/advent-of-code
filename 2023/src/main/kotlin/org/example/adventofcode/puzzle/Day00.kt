package org.example.adventofcode.puzzle

import org.example.adventofcode.util.Utils

object Day00 {
    fun part1(filePath: String): Int {
        val fileLines = Utils.loadFromFile<String>(filePath)
        return 1
    }

    fun part2(filePath: String): Int {
        val fileLines = Utils.loadFromFile<String>(filePath)
        return 1
    }
}

fun main() {
    println("Part 1 example solution is: ${Day00.part1("/day10_example.txt")}")
    println("Part 1 main solution is: ${Day00.part1("/day00.txt")}")
    println("Part 2 example solution is: ${Day00.part2("/day10_example.txt")}")
    println("Part 2 main solution is: ${Day00.part2("/day00.txt")}")
}