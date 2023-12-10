package org.example.adventofcode.puzzle

import org.example.adventofcode.util.FileLoader
import java.util.stream.Collectors
import kotlin.math.abs

object Day09 {

    fun part1(filePath: String): Int {
        val lines = FileLoader.loadFromFile<String>(filePath)
        val instructions = loadInstructions(lines)
        val tailHistorySet = processInstructions(instructions)
        return tailHistorySet.size
    }

    fun part2(filePath: String): Int {
        val lines = FileLoader.loadFromFile<String>(filePath)
        val instructions = loadInstructions(lines)
        val tailHistorySet = processInstructionsPart2(instructions)
        return tailHistorySet.size
    }

    private fun loadInstructions(lines: List<String>): List<Instruction> {
        return lines.stream().map {
            val lineParts = it.split(" ")
            Instruction(lineParts[0], lineParts[1].toInt())
        }.collect(Collectors.toList())
    }

    private fun processInstructions(instructions: List<Instruction>): Set<String> {
        val headPos = Position(0, 0)
        var tailPos = Position(0, 0)
        val tailHistorySet = HashSet<String>()
        tailHistorySet.add(tailPos.toString())
        for (instruction in instructions) {

            for (i in 0 until instruction.numberOfSpaces) {
                // Move Head
                if(instruction.direction == "L") {
                    headPos.x -= 1
                    tailPos = getNewTailPosition(headPos, tailPos)
                } else if (instruction.direction == "R") {
                    headPos.x += 1
                } else if(instruction.direction == "U") {
                    headPos.y += 1
                } else if(instruction.direction == "D") {
                    headPos.y -= 1
                }

                // Move Tail
                tailPos = getNewTailPosition(headPos, tailPos)
                tailHistorySet.add(tailPos.toString())
            }

        }

        return tailHistorySet
    }

    private fun processInstructionsPart2(instructions: List<Instruction>): Set<String> {
        val headPos = Position(0, 0)
        var tail1 = Position(0, 0)
        var tail2 = Position(0, 0)
        var tail3 = Position(0, 0)
        var tail4 = Position(0, 0)
        var tail5 = Position(0, 0)
        var tail6 = Position(0, 0)
        var tail7 = Position(0, 0)
        var tail8 = Position(0, 0)
        var tail9 = Position(0, 0)

        val tailHistorySet = HashSet<String>()
        tailHistorySet.add(tail9.toString())
        for (instruction in instructions) {
            for (i in 0 until instruction.numberOfSpaces) {
                // Move Head
                if(instruction.direction == "L") {
                    headPos.x -= 1
                } else if (instruction.direction == "R") {
                    headPos.x += 1
                } else if(instruction.direction == "U") {
                    headPos.y += 1
                } else if(instruction.direction == "D") {
                    headPos.y -= 1
                }

                // Move Tail
                tail1 = getNewTailPosition(headPos, tail1)
                tail2 = getNewTailPosition(tail1, tail2)
                tail3 = getNewTailPosition(tail2, tail3)
                tail4 = getNewTailPosition(tail3, tail4)
                tail5 = getNewTailPosition(tail4, tail5)
                tail6 = getNewTailPosition(tail5, tail6)
                tail7 = getNewTailPosition(tail6, tail7)
                tail8 = getNewTailPosition(tail7, tail8)
                tail9 = getNewTailPosition(tail8, tail9)
                tailHistorySet.add(tail9.toString())
            }

        }

        return tailHistorySet
    }

    private fun getNewTailPosition(headPos: Position, tailPos: Position): Position {
        val differenceX = headPos.x - tailPos.x
        val differenceY = headPos.y - tailPos.y
        val paddedX = if(differenceX<0) differenceX+1 else differenceX-1
        val paddedY = if(differenceY<0) differenceY+1 else differenceY-1

        val newTailPos: Position = if(abs(differenceX) > 1 && abs(differenceY) > 1) {
            Position(tailPos.x+paddedX, tailPos.y+paddedY)
        } else if(abs(differenceX) >= 1 && abs(differenceY) > 1) {
            Position(tailPos.x+differenceX, tailPos.y+paddedY)
        } else if (abs(differenceX) > 1 && abs(differenceY) >= 1) {
            Position(tailPos.x+paddedX, tailPos.y+differenceY)
        } else if(abs(differenceX) > 1) {
            Position(tailPos.x+paddedX, tailPos.y)
        } else if (abs(differenceY) > 1) {
            Position(tailPos.x, tailPos.y+paddedY)
        } else {
            tailPos
        }

        return newTailPos
    }

    data class Instruction(
        val direction: String,
        val numberOfSpaces: Int
    )

    data class Position(
        var x: Int,
        var y: Int
    ) {
        override fun toString(): String {
            return "${x},${y}"
        }
    }
}

fun main() {
    println("Part 1 example solution is: ${Day09.part1("/day09_example.txt")}")
    println("Part 1 main solution is: ${Day09.part1("/day09.txt")}")
    println("Part 2 example solution is: ${Day09.part2("/day09_example2.txt")}")
    println("Part 2 main solution is: ${Day09.part2("/day09.txt")}")
}