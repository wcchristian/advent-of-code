package org.example.adventofcode.puzzle

import org.example.adventofcode.util.FileLoader

object Day03 {
    fun part1(filePath: String): Int {
        val lines = FileLoader.loadFromFile<String>(filePath)
        var prioritySum = 0
        for (line in lines) {
            val compartmentSize = line.length / 2
            val ruckSack1 = line.substring(0, compartmentSize)
            val ruckSack2 = line.substring(compartmentSize)

            var dupeChar: Char? = null
            for (char in ruckSack1) {
                if (ruckSack2.contains(char, ignoreCase = false)) {
                    dupeChar = char
                    break;
                }
            }
            val itemValue = if (dupeChar!!.isLowerCase()) dupeChar.code - 96 else dupeChar.code - 64 + 26 // Using ASCII to get char values
            prioritySum += itemValue
        }
        return prioritySum
    }

    fun part2(filePath: String): Int {
        val lines = FileLoader.loadFromFile<String>(filePath)
        var prioritySum = 0
        for (idx in lines.indices step 3) {
            val elf1 = lines[idx]
            val elf2 = lines[idx+1]
            val elf3 = lines[idx+2]

            var dupeChar: Char? = null
            for (char in elf1) {
                if (elf2.contains(char, ignoreCase = false) && elf3.contains(char, ignoreCase = false)) {
                    dupeChar = char
                    break;
                }
            }

            val itemValue = if (dupeChar!!.isLowerCase()) dupeChar.code - 96 else dupeChar.code - 64 + 26 // Using ASCII to get char values
            prioritySum += itemValue
        }

        return prioritySum
    }
}

fun main() {
    println("Part 1 example solution is: ${Day03.part1("/day03_example.txt")}")
    println("Part 1 main solution is: ${Day03.part1("/day03.txt")}")
    println("Part 2 example solution is: ${Day03.part2("/day03_example.txt")}")
    println("Part 2 main solution is: ${Day03.part2("/day03.txt")}")
}