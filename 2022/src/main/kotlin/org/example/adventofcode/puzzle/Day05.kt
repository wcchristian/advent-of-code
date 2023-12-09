package org.example.adventofcode.puzzle

import org.example.adventofcode.util.FileLoader
import java.util.*
import kotlin.collections.ArrayList

object Day05 {

    fun part1(filePath: String): String {
        val lines = FileLoader.loadFromFile<String>(filePath)
        val stacks = readBaseStacks(lines)
        val instructions = readInstructions(lines)

        for (instruction in instructions) {
            for (i in 0 until instruction.count) {
                var letter: String
                try {
                letter = stacks[instruction.from-1].pop()
                } catch (e: EmptyStackException) {
                    continue
                }
                stacks[instruction.to-1].push(letter)
            }
        }

        var result = ""
        for (stack in stacks) {
            result += stack.pop()
        }
        return result
    }

    fun part2(filePath: String): String {
        val lines = FileLoader.loadFromFile<String>(filePath)
        val stacks = readBaseStacks(lines)
        val instructions = readInstructions(lines)

        for (instruction in instructions) {
            val moveQueue = ArrayList<String>()
            for (i in 0 until instruction.count) {
                try {
                    moveQueue.add(stacks[instruction.from-1].pop())
                } catch (e: EmptyStackException) {
                    continue
                }
            }

            moveQueue.reverse()
            for (item in moveQueue) {
                stacks[instruction.to-1].push(item)
            }
        }

        var result = ""
        for (stack in stacks) {
            result += stack.pop()
        }
        return result
    }


    fun readBaseStacks(lines: List<String>): List<Stack<String>> {
        val listOfStacks = ArrayList<Stack<String>>()
        val stackConfigLines = ArrayList<String>()

        for (line in lines) {
            if (line.isBlank()) {
                break;
            }
            stackConfigLines.add(line)
        }

        val numberStacks = stackConfigLines.last().trim().split(" ").last().toInt()
        stackConfigLines.reverse()
        stackConfigLines.removeAt(0)

        for (i in 0 until numberStacks) {
            listOfStacks.add(Stack())
        }

        for (line in stackConfigLines) {
            val chunks = line.chunked(4)
            for (i in chunks.indices) {
                if(chunks[i].isNotBlank()) {
                    val letter = chunks[i].removePrefix("[").removeSuffix("] ").removeSuffix("]")
                    listOfStacks[i].push(letter)
                }
            }
        }

        return listOfStacks
    }

    fun readInstructions(lines: List<String>): List<Instruction> {
        val instructionList = ArrayList<Instruction>()
        for(line in lines) {
            if (line.startsWith("move")) {
                val numbers = line.split("move ", "from ", "to ")
                instructionList.add(Instruction(numbers[1].trim().toInt(), numbers[2].trim().toInt(), numbers[3].trim().toInt()))
            }
        }

        return instructionList
    }

    data class Instruction(
        val count: Int,
        val from: Int,
        val to: Int
    )
}

fun main() {
    println("Part 1 example solution is: ${Day05.part1("/day05_example.txt")}")
    println("Part 1 main solution is: ${Day05.part1("/day05.txt")}")
    println("Part 2 example solution is: ${Day05.part2("/day05_example.txt")}")
    println("Part 2 main solution is: ${Day05.part2("/day05.txt")}")
}