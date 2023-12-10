package org.example.adventofcode.puzzle

import org.example.adventofcode.util.FileLoader
import java.util.Arrays

object Day10 {

    fun part1(filePath: String): Int {
        val lines = FileLoader.loadFromFile<String>(filePath)
        val targetCycles = listOf(20, 60, 100, 140, 180, 220)
        val signalStrengths = ArrayList<Int>()
        var registerX = 1
        var clockCycles = 0
        var cyclesToRun = 0
        var valueAtTheEndOfCycleToAdd = 0

        for (line in lines) {
            if(line.trim() == "noop") {
                cyclesToRun = 1
                valueAtTheEndOfCycleToAdd = 0
            } else if (line.startsWith("addx")) {
                val value = line.split(" ")[1].toInt()
                valueAtTheEndOfCycleToAdd = value
                cyclesToRun = 2
            }

            for(i in 0 until cyclesToRun) {
                clockCycles += 1
                if(targetCycles.contains(clockCycles)) {
                    signalStrengths.add(clockCycles*registerX)
                }
            }

            registerX += valueAtTheEndOfCycleToAdd
        }

        return signalStrengths.sum()
    }

    fun part2(filePath: String): Int {
        val lines = FileLoader.loadFromFile<String>(filePath)
        val targetCycles = listOf(40, 80, 120, 160, 200, 240)
        val signalStrengths = ArrayList<Int>()
        var registerX = 1
        var clockCycles = 0
        var cyclesToRun = 0
        var valueAtTheEndOfCycleToAdd = 0
        var currentLine = ""
        var screen = ArrayList<String>()

        for (line in lines) {
            if(line.trim() == "noop") {
                cyclesToRun = 1
                valueAtTheEndOfCycleToAdd = 0
            } else if (line.startsWith("addx")) {
                val value = line.split(" ")[1].toInt()
                valueAtTheEndOfCycleToAdd = value
                cyclesToRun = 2
            }

            val lineNumber = 0
            for(i in 0 until cyclesToRun) {
                if(targetCycles.contains(clockCycles)) {
                    screen.add(currentLine)
                    currentLine = ""
                }

                val currentCycleIndex = clockCycles % 40
                if (registerX-1 == currentCycleIndex || registerX == currentCycleIndex || registerX+1 == currentCycleIndex) {
                    currentLine += "#"
                } else {
                    currentLine += "."
                }
                clockCycles += 1
            }

            registerX += valueAtTheEndOfCycleToAdd
        }

        // Last Line
        screen.add(currentLine)

        print("\n\n")
        for (line in screen) {
            println(line)
        }
        print("\n\n")

        return signalStrengths.sum()
    }
}

fun main() {
    println("Part 1 example solution is: ${Day10.part1("/day10_example.txt")}")
    println("Part 1 main solution is: ${Day10.part1("/day10.txt")}")
    println("Part 2 example solution is:")
    Day10.part2("/day10_example.txt")
    println("Part 2 main solution is:")
    Day10.part2("/day10.txt")
}