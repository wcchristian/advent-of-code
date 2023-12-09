package org.example.adventofcode.puzzle

import org.example.adventofcode.util.FileLoader

object Day01 {
    fun part1(filePath: String): Int {
        var elfList = getElfList(filePath)
        elfList = elfList.sortedDescending()
        return elfList.first()
    }

    fun part2(filePath: String): Int {
        var elfList = getElfList(filePath)
        elfList = elfList.sortedDescending()
        return elfList[0] + elfList[1] + elfList[2]
    }

    fun getElfList(filePath: String): List<Int> {
        val fileLines = FileLoader.loadFromFile<String>(filePath)

        var currentCount = 0
        val elves = ArrayList<Int>()
        for (line in fileLines) {
            if (line.isBlank()) {
                elves.add(currentCount)
                currentCount = 0
            } else {
                currentCount += line.toInt()
            }
        }

        // last line
        elves.add(currentCount)

        return elves
    }
}

fun main() {
    println("Part 1 example solution is: ${Day01.part1("/day01_example.txt")}")
    println("Part 1 main solution is: ${Day01.part1("/day01.txt")}")
    println("Part 2 example solution is: ${Day01.part2("/day01_example.txt")}")
    println("Part 2 main solution is: ${Day01.part2("/day01.txt")}")
}