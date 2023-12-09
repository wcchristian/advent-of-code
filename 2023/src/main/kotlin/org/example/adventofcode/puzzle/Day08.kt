package org.example.adventofcode.puzzle

import org.example.adventofcode.util.FileLoader
import java.util.function.Predicate

object Day08 {
    fun part1(filePath: String): Long {
        val fileLines = FileLoader.loadFromFile<String>(filePath)
        val nodeMap = loadMap(fileLines)
        return walkMap(nodeMap, { it == "AAA" }, {it != "ZZZ"})
    }

    fun part2(filePath: String): Long {
        val fileLines = FileLoader.loadFromFile<String>(filePath)
        val nodeMap = loadMap(fileLines)
        return ghostWalkMap(nodeMap)
    }
    
    private fun loadMap(fileLines: List<String>): ElfMap {
        val instructions = fileLines.first()

        val nodes = fileLines.subList(2, fileLines.size).map {
            val match = Regex("(\\w+) = \\((\\w+), (\\w+)\\)").find(it)
            val key = match!!.groupValues[1]
            val left = match.groupValues[2]
            val right = match.groupValues[3]
            key to Pair(left, right)
        }.toMap()
        return ElfMap(instructions, nodes as NodeList)
    }

    private fun walkMap(elfMap: ElfMap, currentNodeTest: Predicate<String>, destinationNodeTest: Predicate<String>): Long {
        var currentNode = elfMap.nodes.keys.first { currentNodeTest.test(it) }
        var currentSteps = 0
        var instructionIndex = 0

        while (destinationNodeTest.test(currentNode)) {
            if(instructionIndex >= elfMap.instructions.length) {
                instructionIndex = 0
            }

            val instruction = elfMap.instructions[instructionIndex]
            currentNode = if (instruction == 'L') {
                elfMap.nodes[currentNode]!!.first
            } else {
                elfMap.nodes[currentNode]!!.second
            }

            instructionIndex++
            currentSteps++
        }

        return currentSteps.toLong()
    }

    private fun ghostWalkMap(elfMap: ElfMap): Long {
        val distances = elfMap.nodes.keys
            .filter { it.endsWith("A") }
            .toMutableList()
            .map { startingNode -> walkMap(elfMap, {it == startingNode}, {!it.endsWith("Z")}) }
            .toList()

        return distances.reduce { acc, i -> acc * i / findGCD(acc, i) }
    }

    private fun findGCD(a: Long, b: Long): Long {
        return if (b == 0L) a else findGCD(b, a % b)
    }
}

typealias NodeList = HashMap<String, Pair<String, String>>

data class ElfMap(
    val instructions: String,
    val nodes: NodeList,
)

fun main() {
    println("Part 1 example solution is: ${Day08.part1("/day08_example.txt")}")
    println("Part 1 example 2 solution is: ${Day08.part1("/day08_example2.txt")}")
    println("Part 1 main solution is: ${Day08.part1("/day08.txt")}")
    println("Part 2 example solution is: ${Day08.part2("/day08p2_example.txt")}")
    println("Part 2 main solution is: ${Day08.part2("/day08.txt")}")
}