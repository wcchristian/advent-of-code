package org.example.adventofcode.puzzle

import org.example.adventofcode.util.FileLoader

object Day09 {
    fun part1(filePath: String): Int {
        val fileLines = FileLoader.loadFromFile<String>(filePath)
        val trees = loadTrees(fileLines).map {
            extrapolateDataRight(it)
        }
//        trees.forEach { it.print() }
        return trees.sumOf { it.first().last() }
    }

    fun part2(filePath: String): Int {
        val fileLines = FileLoader.loadFromFile<String>(filePath)
        val trees = loadTrees(fileLines).map {
            extrapolateDataLeft(it)
        }
//        trees.forEach { it.print() }
        return trees.sumOf { it.first().first() }
    }

    private fun loadTrees(fileLines: List<String>): ArrayList<Tree> {
        return ArrayList(fileLines.map { line -> loadTree(line.split(" ").map { it.toInt() }) })
    }

    private fun loadTree(line: List<Int>): Tree {
        val tree = arrayListOf<ArrayList<Int>>()
        var currentLine = ArrayList(line)
        tree.add(currentLine)
        while (currentLine.any { it != 0 }) {
            val newLine = arrayListOf<Int>()
            for (i in 0 until currentLine.size - 1) {
                val result = currentLine[i+1] - currentLine[i]
                newLine.add(result)
            }
            currentLine = newLine
            tree.add(currentLine)
        }
        return tree
    }

    private fun extrapolateDataLeft(tree: Tree): Tree {
        val reversedTree = tree.reversed()
        reversedTree.forEachIndexed { index, ints ->
            if(ints.all { it == 0 }) {
                ints.add(0, 0)
            } else {
                ints.add(0, ints.first() - reversedTree[index - 1].first())
            }
        }
        return ArrayList(reversedTree.reversed())
    }

    private fun extrapolateDataRight(tree: Tree): Tree {
        val reversedTree = tree.reversed()
        reversedTree.forEachIndexed { index, ints ->
            if(ints.all { it == 0 }) {
                ints.add(0)
            } else {
                ints.add(ints.last() + reversedTree[index - 1].last())
            }
        }
        return ArrayList(reversedTree.reversed())
    }
}

typealias Tree = ArrayList<ArrayList<Int>>

fun Tree.print() {
    for(i in 0 until this.size) {
        print(" ".repeat(i))
        for(j in 0 until this[i].size) {
            print(this[i][j].toString() + " ")
        }
        println()
    }
}

fun main() {
    println("Part 1 example solution is: ${Day09.part1("/day09_example.txt")}")
    println("Part 1 main solution is: ${Day09.part1("/day09.txt")}")
    println("Part 2 example solution is: ${Day09.part2("/day09_example.txt")}")
    println("Part 2 main solution is: ${Day09.part2("/day09.txt")}")
}