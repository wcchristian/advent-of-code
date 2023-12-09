package org.example.adventofcode.puzzle

import org.example.adventofcode.util.FileLoader
import java.util.*
import kotlin.collections.ArrayList
import kotlin.math.sign

object Day06 {

    fun part1(filePath: String): Int {
        val lines = FileLoader.loadFromFile<String>(filePath)
        val signalLine = lines[0]

        for (i in 3 until signalLine.length) {
            var foundDupes = false
            val charList = listOf(signalLine[i], signalLine[i-1], signalLine[i-2], signalLine[i-3])
            for (char in charList) {
                val charListWithoutCurrentChar = ArrayList(charList)
                charListWithoutCurrentChar.remove(char)
               if (charListWithoutCurrentChar.contains(char)) {
                   foundDupes = true
                   break
               }
            }

            if (!foundDupes) {
                return i+1
            }
        }
        return -1
    }

    fun part2(filePath: String): Int {
        val lines = FileLoader.loadFromFile<String>(filePath)
        val signalLine = lines[0]

        for (i in 13 until signalLine.length) {
            var foundDupes = false
            val charList = ArrayList<Char>()
            for (j in 0 until 14) {
                charList.add(signalLine[i-j])
            }

            for (char in charList) {
                val charListWithoutCurrentChar = ArrayList(charList)
                charListWithoutCurrentChar.remove(char)
                if (charListWithoutCurrentChar.contains(char)) {
                    foundDupes = true
                    break
                }
            }

            if (!foundDupes) {
                return i+1
            }
        }
        return -1
    }
}

fun main() {
    println("Part 1 example solution is: ${Day06.part1("/day06_example.txt")}")
    println("Part 1 main solution is: ${Day06.part1("/day06.txt")}")
    println("Part 2 example solution is: ${Day06.part2("/day06_example.txt")}")
    println("Part 2 main solution is: ${Day06.part2("/day06.txt")}")
}