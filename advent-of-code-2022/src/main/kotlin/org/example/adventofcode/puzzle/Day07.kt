package org.example.adventofcode.puzzle

import org.example.adventofcode.util.FileLoader
import java.util.*
import java.util.stream.Collectors
import kotlin.collections.ArrayList
import kotlin.collections.HashMap
import kotlin.math.sign

object Day07 {

    fun part1(filePath: String): Long {
        val lines = FileLoader.loadFromFile<String>(filePath)
        var tree = buildDirectoryTree(lines)
        tree = setDirectorySizes(tree)
        val nodes = getNodesUnderOverSize(tree, 100_000L, false)
        return nodes.sumOf { it.size }
    }

    fun part2(filePath: String): Long {
        val lines = FileLoader.loadFromFile<String>(filePath)
        var tree = buildDirectoryTree(lines)
        tree = setDirectorySizes(tree)

        val spaceAvailable = 70000000 - tree.size
        val spaceNeeded = 30000000 - spaceAvailable

        val nodes = getNodesUnderOverSize(tree, spaceNeeded, true)
        return nodes.minOf {it.size}
    }

    private fun buildDirectoryTree(lines: List<String>): DirectoryStructureNode {
        val fullList = DirectoryStructureNode("/", 0, null, ArrayList())
        var currentPlace = fullList
        for (line in lines) {
            if (line.startsWith("$ cd /")) {
                currentPlace = fullList
            } else if (line.startsWith("$ cd ..")) {
                currentPlace = currentPlace.parent!!
            } else if (line.startsWith("$ cd ")) {
                val name = line.split(" ")[2]
                currentPlace = currentPlace.children.find { it.name == name }!!
            } else if (line.startsWith("dir")) {
                val name = line.split(" ")[1]
                currentPlace.children.add(
                    DirectoryStructureNode(name, 0, currentPlace, ArrayList())
                )
            } else if (line[0].isDigit()) {
                val lineParts = line.split(" ")
                val size = lineParts[0]
                val name = lineParts[1]
                currentPlace.children.add(
                    DirectoryStructureNode(name, size.toLong(), currentPlace, ArrayList())
                )
            }
        }
        return fullList
    }

    private fun setDirectorySizes(tree: DirectoryStructureNode): DirectoryStructureNode {
        if(tree.children.size == 0) {
            return tree
        } else {
            var size = 0L
            for(child in tree.children) {
                setDirectorySizes(child)
                size += child.size
            }
            tree.size = size
        }

        return tree
    }

    private fun getNodesUnderOverSize(tree: DirectoryStructureNode, size: Long, isOver: Boolean): List<DirectoryStructureNode> {
        val nodeList = ArrayList<DirectoryStructureNode>()
        for (child in tree.children) {
            nodeList.addAll(getNodesUnderOverSize(child, size, isOver))
            if((isOver && child.size > size) || !isOver && child.size < size) {
                nodeList.add(child)
            }
        }

        return nodeList.stream().filter {
            it.children.size > 0
        }.collect(Collectors.toList())
    }
}

data class DirectoryStructureNode(
    val name: String,
    var size: Long,
    val parent: DirectoryStructureNode?,
    val children: ArrayList<DirectoryStructureNode>
) {
    override fun toString(): String = "Name: ${name} size: ${size} children: ${children.size}"
}


fun main() {
    println("Part 1 example solution is: ${Day07.part1("/day07_example.txt")}")
    println("Part 1 main solution is: ${Day07.part1("/day07.txt")}")
    println("Part 2 example solution is: ${Day07.part2("/day07_example.txt")}")
    println("Part 2 main solution is: ${Day07.part2("/day07.txt")}")
}