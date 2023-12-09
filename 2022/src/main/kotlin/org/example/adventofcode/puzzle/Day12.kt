package org.example.adventofcode.puzzle

import org.example.adventofcode.util.FileLoader
import java.lang.IllegalArgumentException

object Day12 {

    fun part1(filePath: String): Int {
        val lines = FileLoader.loadFromFile<String>(filePath)
        val map = initializeMap(lines)
        val startingNode = findCharInMap('S', map)
        return findShortestPathDistanceToEnd(map, startingNode)
    }

    fun part2(filePath: String): Int {
        val lines = FileLoader.loadFromFile<String>(filePath)
        val map = initializeMap(lines)
        val startingNodes = findLowestElevationNodes(map)
        val shortestDistancesToEnd = ArrayList<Int>()

        for (i in startingNodes.indices) {
            print("Node ${i}/${startingNodes.size}\n")
            shortestDistancesToEnd.add(findShortestPathDistanceToEnd(map, startingNodes[i]))
        }

        return shortestDistancesToEnd.min()
    }

    fun findShortestPathDistanceToEnd(map: List<List<Node>>, startingNode: Node): Int {
        val unvisitedNodes = initializeUnvisitedNodes(map)

        //initialize starting node distance to zero
        startingNode.tentativeDistanceValue = 0
        var currentNode = startingNode

        while (unvisitedNodes.size > 0) {
            // calculate tentative distance of each neighbor of the current node
            val neighbors = getNeighbors(currentNode, map)
            val newDistance = currentNode.tentativeDistanceValue+1
            for (neighbor in neighbors) {
                val elevationDifference = neighbor.char.code - currentNode.char.code
                if(elevationDifference <= 1 || neighbor.char == 'E' || (currentNode.char == 'S' && neighbor.char == 'a')) {
                    if(newDistance < neighbor.tentativeDistanceValue || neighbor.tentativeDistanceValue == -1) {
                        neighbor.tentativeDistanceValue = newDistance
                    }
                }
            }

            // mark current node as visited and remove it from the unvisited set
            unvisitedNodes.remove(currentNode)

            // if the destination node is marked visited, we are done else grab the smallest tentative value
            if(currentNode.char == 'E') {
                break
            } else {
                currentNode = unvisitedNodes
                    .filter {
                        it.tentativeDistanceValue != -1
                    }.minBy { it.tentativeDistanceValue }
            }
        }
        return currentNode.tentativeDistanceValue
    }

    fun findLowestElevationNodes(map: List<List<Node>>): List<Node> {
        val lowestElevationNodes = ArrayList<Node>()
        for (row in map) {
            for (node in row) {
                if(node.char == 'S' || node.char == 'a') {
                    lowestElevationNodes.add(node)
                }
            }
        }
        return lowestElevationNodes
    }

    fun printGridDistances(map: List<List<Node>>) {
        for (row in map) {
            for (node in row) {
                if(node.tentativeDistanceValue == -1) {
                    print("x ")
                } else {
                    print(node.tentativeDistanceValue.toString() + " ")
                }
            }
            println()
        }
    }

    fun getNeighbors(currentNode: Node, map: List<List<Node>>): ArrayList<Node> {
        val neighbors = ArrayList<Node>()
        if(currentNode.position.y > 0) {
            neighbors.add(map[currentNode.position.y-1][currentNode.position.x])
        }
        if(currentNode.position.y < map.size-1) {
            neighbors.add(map[currentNode.position.y+1][currentNode.position.x])
        }
        if(currentNode.position.x > 0) {
            neighbors.add(map[currentNode.position.y][currentNode.position.x-1])
        }
        if(currentNode.position.x < map[0].size-1) {
            neighbors.add(map[currentNode.position.y][currentNode.position.x+1])
        }
        return neighbors
    }

    fun findCharInMap(char: Char, map: ArrayList<ArrayList<Node>>): Node {
        for (row in map) {
            for (node in row) {
                if(node.char == char) {
                    return node
                }
            }
        }
        throw IllegalArgumentException("Map must contain a starting position")
    }

    fun initializeUnvisitedNodes(map: List<List<Node>>): ArrayList<Node> {
        val unvisitedNodes = ArrayList<Node>()
        for (row in map) {
            for (node in row) {
                unvisitedNodes.add(node)
            }
        }
        return unvisitedNodes
    }

    fun initializeMap(lines: List<String>): ArrayList<ArrayList<Node>> {
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

    data class Position(
        val x: Int,
        val y: Int
    )

    data class Node(
        val position: Position,
        var tentativeDistanceValue: Int = -1, // using -1 to signify unset
        val char: Char
    )
}

fun main() {
    println("Part 1 example solution is: ${Day12.part1("/day12_example.txt")}")
    println("Part 1 main solution is: ${Day12.part1("/day12.txt")}")
    println("Part 2 example solution is: ${Day12.part2("/day12_example.txt")}")
    println("Part 2 main solution is: ${Day12.part2("/day12.txt")}")
}