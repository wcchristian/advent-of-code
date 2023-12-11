package org.example.adventofcode.puzzle

import org.example.adventofcode.util.FileLoader
import java.lang.IllegalArgumentException
import kotlin.math.abs

object Day10 {
    fun part1(filePath: String): Int {
        val fileLines = FileLoader.loadFromFile<String>(filePath)
        val map = initializeMap(fileLines)
        val startingNode = findCharInMap('S', map)
        val endMap = calcGridDistances(map, startingNode)
        return endMap.maxOf { it.maxOf { it.tentativeDistanceValue } }
    }

    fun part2(filePath: String): Int {
        val fileLines = FileLoader.loadFromFile<String>(filePath)
        return countWithin(fileLines)
    }

    private fun countWithin(fileLines: List<String>): Int {
        val pipes = "|LJ"
        var count = 0
        val map = fileLines.map { it.toCharArray().toList() }
        val loop = getLoop(map)

        for (y in map.indices) {
            var inside = false
            for (x in map.first().indices) {
                if (Position(x, y) in loop && map[y][x] in pipes) {
                    inside = !inside
                }
                if (Position(x, y) !in loop && inside) {
                    count++
                }
            }
        }

        return count
    }

    private fun getLoop(grid: List<List<Char>>): Set<Position> {
        var start = Position(0, 0)
        for (y in grid.indices) {
            for (x in grid[y].indices) {
                if (grid[y][x] == 'S') {
                    start = Position(x, y)
                }
            }
        }

        val toVisit = ArrayDeque(listOf(start))
        val visited = mutableSetOf(start)

        while (toVisit.isNotEmpty()) {
            val current = toVisit.removeLast()
            current.validNeighbours(grid)
                .filter { n -> current.isConnected(grid, n) && n !in visited }
                .forEach { n ->
                    toVisit.add(n)
                    visited.add(n)
                }
        }

        return visited
    }

    private fun Position.validNeighbours(map: List<List<Char>>) = neighbours().filter { it.y in map.indices && it.x in map.first().indices }

    private fun Position.isConnected(map: List<List<Char>>, other: Position): Boolean {
        return when {
            map[y][x] == 'S' -> other.isConnected(map, this)
            map[y][x] == '|' -> other.x == x && abs(other.y - y) == 1
            map[y][x] == '-' -> other.y == y && abs(other.x - x) == 1
            map[y][x] == 'L' -> (other.y == y - 1 && other.x == x) || (other.x == x + 1 && other.y == y)
            map[y][x] == 'J' -> (other.y == y - 1 && other.x == x) || (other.x == x - 1 && other.y == y)
            map[y][x] == '7' -> (other.y == y + 1 && other.x == x) || (other.x == x - 1 && other.y == y)
            map[y][x] == 'F' -> (other.y == y + 1 && other.x == x) || (other.x == x + 1 && other.y == y)
            else              -> false
        }
    }

    private fun initializeUnvisitedNodes(map: List<List<Node>>): ArrayList<Node> {
        val unvisitedNodes = ArrayList<Node>()
        for (row in map) {
            for (node in row) {
                unvisitedNodes.add(node)
            }
        }
        return unvisitedNodes
    }

    private fun findCharInMap(char: Char, map: ArrayList<ArrayList<Node>>): Node {
        for (row in map) {
            for (node in row) {
                if(node.char == char) {
                    return node
                }
            }
        }
        throw IllegalArgumentException("Map must contain a starting position")
    }

    private fun initializeMap(lines: List<String>): ArrayList<ArrayList<Node>> {
        val map = ArrayList<ArrayList<Node>>()

        for (y in lines.indices) {
            val row = ArrayList<Node>()
            for (x in lines[y].indices) {
                row.add(Node(Position(x, y), tentativeDistanceValue = -1, char = lines[y][x])) // using -1 to signify unset
            }
            map.add(row)
        }

        return map
    }

    private fun calcGridDistances(map: List<List<Node>>, startingNode: Node): List<List<Node>> {
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

    fun printGridDistances(map: List<List<Node>>, delimiter: String = " ") {
        for (row in map) {
            for (node in row) {
                print(node.tentativeDistanceValue.toString() + delimiter)
            }
            println()
        }
    }
    fun printGrid(map: List<List<Node>>, delimiter: String = " ") {
        for (row in map) {
            for (node in row) {
            print(node.char.toString() + delimiter)
            }
            println()
        }
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
) {
    fun neighbours(): List<Position> {
        return listOf(
            Position(x - 1, y),
            Position(x + 1, y),
            Position(x, y - 1),
            Position(x, y + 1),
        )
    }
}

data class Node(
    val position: Position,
    var tentativeDistanceValue: Int = -1, // -1 means unset
    val char: Char
)

fun main() {
//    println("Part 1 example solution is: ${Day10.part1("/day10_example.txt")}")
//    println("Part 1 example 2 solution is: ${Day10.part1("/day10_example2.txt")}")
//    println("Part 1 main solution is: ${Day10.part1("/day10.txt")}")

    println("Part 2 example solution is: ${Day10.part2("/day10p2_example.txt")}")
    println("Part 2 example 2 solution is: ${Day10.part2("/day10p2_example2.txt")}")
    println("Part 2 example 3 solution is: ${Day10.part2("/day10p2_example3.txt")}")
    println("Part 2 main solution is: ${Day10.part2("/day10.txt")}")
}