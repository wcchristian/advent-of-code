package org.example.adventofcode.puzzle

import org.example.adventofcode.util.Utils
import java.lang.IllegalArgumentException

object Day10 {
    fun part1(filePath: String): Int {
        val fileLines = Utils.loadFromFile<String>(filePath)
        val grid = buildGrid(fileLines)
        return grid.maxOf { it.maxOf { it.tentativeDistanceValue } }
    }

    fun part2(filePath: String): Int {
        val fileLines = Utils.loadFromFile<String>(filePath)
        val grid = buildGrid(fileLines)
        val pipePositions = getPipePositions(grid)
        return countInsideSpaces(pipePositions, grid)
    }

    private fun countInsideSpaces(pipePositions: Set<Position>, grid: Grid): Int {
        // Looked for some reddit help on this part. Took me a minute to grasp but, if you imagine
        // going through the top half of each "cell" (letter) then these are all vertical walls.
        // then if we go over each point in the entire grid, and can determine that we crossed a boundary
        // we can then say we are "inside". If the current position is NOT in the loop and inside is marked, then we can count it as
        // an "inside" cell.
        // SIDE NOTE: Point in polygon is where I failed AoC last year. Took this one as a learning opportunity :D
        val pipes = "|LJ"
        var count = 0

        for (y in grid.indices) {
            var inside = false
            for (x in grid.first().indices) {
                if (Position(x, y) in pipePositions && grid[y][x].char in pipes) {
                    inside = !inside
                }
                if (Position(x, y) !in pipePositions && inside) {
                    count++
                }
            }
        }

        return count
    }

    private fun getPipePositions(grid: Grid): Set<Position> {
        val pipeLoop = hashSetOf<Position>()
        for(y in grid.indices) {
            for(x in grid.first().indices) {
                if(grid[y][x].tentativeDistanceValue != -1) {
                    pipeLoop.add(grid[y][x].position)
                }
            }
        }
        return pipeLoop
    }

    private fun initializeUnvisitedNodes(grid: Grid): ArrayList<Node> {
        val unvisitedNodes = ArrayList<Node>()
        for (row in grid) {
            for (node in row) {
                unvisitedNodes.add(node)
            }
        }
        return unvisitedNodes
    }

    private fun findStartingPoint(grid: Grid): Node {
        for (row in grid) {
            for (node in row) {
                if(node.char == 'S') {
                    return node
                }
            }
        }
        throw IllegalArgumentException("Map must contain a starting position")
    }

    private fun initializeMap(lines: List<String>): Grid {
        val grid = ArrayList<ArrayList<Node>>()

        for (y in lines.indices) {
            val row = ArrayList<Node>()
            for (x in lines[y].indices) {
                row.add(Node(Position(x, y), tentativeDistanceValue = -1, char = lines[y][x])) // using -1 to signify unset
            }
            grid.add(row)
        }

        return grid
    }

    private fun buildGrid(fileLines: List<String>): Grid {
        val map = initializeMap(fileLines)
        val startingNode = findStartingPoint(map)
        val unvisitedNodes = initializeUnvisitedNodes(map)

        //initialize starting node distance to zero
        startingNode.tentativeDistanceValue = 0
        var currentNode = startingNode

        while (unvisitedNodes.size > 0) {
            // calculate tentative distance of each neighbor of the current node
            val neighbors = getViableNeighbors(currentNode, map)
            val newDistance = currentNode.tentativeDistanceValue+1
            for (neighbor in neighbors) {
                if(newDistance < neighbor.tentativeDistanceValue || neighbor.tentativeDistanceValue == -1) {
                    neighbor.tentativeDistanceValue = newDistance
                }
            }

            // mark current node as visited and remove it from the unvisited set
            unvisitedNodes.remove(currentNode)

            // if the destination node is marked visited, we are done else grab the smallest tentative value
            val viableNodes = unvisitedNodes.filter {
                    it.tentativeDistanceValue != -1
            }

            if(viableNodes.isNotEmpty()) {
                currentNode = viableNodes.minBy { it.tentativeDistanceValue }
            } else {
                break
            }
        }
        return map
    }

    private fun getViableNeighbors(currentNode: Node, map: List<List<Node>>): ArrayList<Node> {
        val neighbors = ArrayList<Node>()
        if(currentNode.position.y > 0 && canGoUp(currentNode.char, map[currentNode.position.y-1][currentNode.position.x].char)) {
            neighbors.add(map[currentNode.position.y-1][currentNode.position.x])
        }
        if(currentNode.position.y < map.size-1 && canGoDown(currentNode.char, map[currentNode.position.y+1][currentNode.position.x].char)) {
            neighbors.add(map[currentNode.position.y+1][currentNode.position.x])
        }
        if(currentNode.position.x > 0 && canGoLeft(currentNode.char, map[currentNode.position.y][currentNode.position.x-1].char)) {
            neighbors.add(map[currentNode.position.y][currentNode.position.x-1])
        }
        if(currentNode.position.x < map[0].size-1 && canGoRight(currentNode.char, map[currentNode.position.y][currentNode.position.x+1].char)) {
            neighbors.add(map[currentNode.position.y][currentNode.position.x+1])
        }
        return neighbors
    }

    private fun canGoUp(currentChar: Char, nextChar: Char) = listOf('|', '7', 'F', 'S').contains(nextChar) && listOf('|', 'J', 'L', 'S').contains(currentChar)
    private fun canGoDown(currentChar: Char, nextChar: Char) = listOf('|', 'J', 'L', 'S').contains(nextChar) && listOf('|', 'F', '7', 'S').contains(currentChar)
    private fun canGoLeft(currentChar: Char, nextChar: Char) = listOf('-', 'L', 'F', 'S').contains(nextChar) && listOf('-', 'J', '7', 'S').contains(currentChar)
    private fun canGoRight(currentChar: Char, nextChar: Char) = listOf('-', 'J', '7', 'S').contains(nextChar) && listOf('-', 'L', 'F', 'S').contains(currentChar)
}

data class Position(
    val x: Int,
    val y: Int
)

data class Node(
    val position: Position,
    var tentativeDistanceValue: Int = -1, // -1 means unset
    val char: Char
)

typealias Grid = List<List<Node>>

fun main() {
    println("Part 1 example solution is: ${Day10.part1("/day10_example.txt")}")
    println("Part 1 example 2 solution is: ${Day10.part1("/day10_example2.txt")}")
    println("Part 1 main solution is: ${Day10.part1("/day10.txt")}")
    println()
    println("Part 2 example solution is: ${Day10.part2("/day10p2_example.txt")}")
    println("Part 2 example 2 solution is: ${Day10.part2("/day10p2_example2.txt")}")
    println("Part 2 example 3 solution is: ${Day10.part2("/day10p2_example3.txt")}")
    println("Part 2 main solution is: ${Day10.part2("/day10.txt")}")
}