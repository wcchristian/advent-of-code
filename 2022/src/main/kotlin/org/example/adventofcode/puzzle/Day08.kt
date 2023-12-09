package org.example.adventofcode.puzzle

import org.example.adventofcode.util.FileLoader
import kotlin.collections.ArrayList

object Day08 {

    fun part1(filePath: String): Int {
        val lines = FileLoader.loadFromFile<String>(filePath)
        val treeGrid = parse2DArray(lines)
        return findVisibleTrees(treeGrid)
    }

    fun part2(filePath: String): Int {
        val lines = FileLoader.loadFromFile<String>(filePath)
        val treeGrid = parse2DArray(lines)
        return findBestScenicScore(treeGrid)
    }
}

fun findBestScenicScore(treeGrid: List<List<Int>>): Int {
    var scenicScore = 0
    for(x in treeGrid.indices) {
        for (y in treeGrid[x].indices) {
            val currentScenicScore = findScenicScore(x, y, treeGrid)
            if(currentScenicScore > scenicScore) scenicScore = currentScenicScore
        }
    }
    return scenicScore
}

fun findVisibleTrees(treeGrid: List<List<Int>>): Int {
    var visibleTreeCount = 0
    for(x in treeGrid.indices) {
        for (y in treeGrid[x].indices) {
            if(checkVisibility(xIndex = x, yIndex = y, treeGrid = treeGrid)) {
                visibleTreeCount += 1
            }
        }
    }

    return visibleTreeCount
}

fun findScenicScore(xIndex: Int, yIndex: Int, treeGrid: List<List<Int>>): Int {
    val currentTreeValue = treeGrid[yIndex][xIndex]
    var scenicScoreUp = 0
    var scenicScoreDown = 0
    var scenicScoreLeft = 0
    var scenicScoreRight = 0

    // check up
    for (i in yIndex-1 downTo 0) {
        scenicScoreUp += 1
        if (currentTreeValue <= treeGrid[i][xIndex]) {
            break
        }
    }

    // check down
    for (i in yIndex+1 until treeGrid.size) {
        scenicScoreDown += 1
        if (currentTreeValue <= treeGrid[i][xIndex]) {
            break
        }
    }

    // check left
    for (i in xIndex-1 downTo 0) {
        scenicScoreLeft += 1
        if (currentTreeValue <= treeGrid[yIndex][i]) {
            break
        }
    }

    // check right
    for (i in xIndex+1 until treeGrid[0].size) {
        scenicScoreRight += 1
        if (currentTreeValue <= treeGrid[yIndex][i]) {
            break
        }
    }

    return scenicScoreUp * scenicScoreDown * scenicScoreLeft * scenicScoreRight
}

fun checkVisibility(xIndex: Int, yIndex: Int, treeGrid: List<List<Int>>): Boolean {
    val currentTreeValue = treeGrid[yIndex][xIndex]
    var isVisibleUp = true
    var isVisibleDown = true
    var isVisibleLeft = true
    var isVisibleRight = true

    // check up
    for (i in yIndex-1 downTo 0) {
        if (currentTreeValue <= treeGrid[i][xIndex]) {
            isVisibleUp = false
            break
        }
    }

    // check down
    for (i in yIndex+1 until treeGrid.size) {
        if (currentTreeValue <= treeGrid[i][xIndex]) {
            isVisibleDown = false
            break
        }
    }

    // check left
    for (i in xIndex-1 downTo 0) {
        if (currentTreeValue <= treeGrid[yIndex][i]) {
            isVisibleLeft = false
            break
        }
    }

    // check right
    for (i in xIndex+1 until treeGrid[0].size) {
        if (currentTreeValue <= treeGrid[yIndex][i]) {
            isVisibleRight = false
            break
        }
    }

    return isVisibleUp || isVisibleDown || isVisibleLeft || isVisibleRight
}

fun parse2DArray(lines: List<String>): List<List<Int>> {
    val result = ArrayList<List<Int>>()
    for (line in lines) {
        val lineList = ArrayList<Int>()
        for(char in line) {
            lineList.add(Character.getNumericValue(char))
        }
        result.add(lineList)
    }
    return result
}


fun main() {
    println("Part 1 example solution is: ${Day08.part1("/day08_example.txt")}")
    println("Part 1 main solution is: ${Day08.part1("/day08.txt")}")
    println("Part 2 example solution is: ${Day08.part2("/day08_example.txt")}")
    println("Part 2 main solution is: ${Day08.part2("/day08.txt")}")
}