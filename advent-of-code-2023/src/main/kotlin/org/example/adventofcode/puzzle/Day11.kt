package org.example.adventofcode.puzzle

import org.example.adventofcode.util.CharGrid
import org.example.adventofcode.util.Utils
import kotlin.math.abs

// Originally had this one solved where I would ACTUALLY expand the grid then process with the expanded grid.
// once I had to refactor due to the nature of part 2, I ended up refactoring part 1 to work the same way.
object Day11 {
    fun part1(filePath: String): Long {
        val grid = Utils.loadCharGridFromFile(filePath)
        return findSumOfDistancesWithFactoredExpansion(grid, 2)
    }

    fun part2(filePath: String): Long {
        val grid = Utils.loadCharGridFromFile(filePath)
        return findSumOfDistancesWithFactoredExpansion(grid, 1_000_000)
    }

    private fun findSumOfDistancesWithFactoredExpansion(grid: CharGrid, expansionFactor: Int): Long {
        val rowExpansionSet = findRowExpansions(grid)
        val columnExpansionSet = findColumnExpansions(grid)
        val galaxyLocations = findGalaxyLocations(grid)
        val galaxyPairs = findGalaxyPairs(galaxyLocations, rowExpansionSet, columnExpansionSet, expansionFactor = expansionFactor)
        return galaxyPairs.sumOf { it.distance }
    }

    private fun findColumnExpansions(grid: CharGrid): Set<Int> {
        val result = HashSet<Int>()
        for(x in grid.first().indices) {
            var isEmpty = true
            for(y in grid.indices) {
                if (grid[y][x] != '.') {
                    isEmpty = false
                    break
                }
            }

            if(isEmpty) {
                result.add(x)
            }
        }

        return result
    }

    private fun findRowExpansions(grid: CharGrid): Set<Int> {
        val result = HashSet<Int>()
        for(y in grid.indices) {
            if(grid[y].all { it == '.' }) {
                result.add(y)
            }
        }
        return result

    }

    private fun findGalaxyLocations(grid: CharGrid): Set<Coordinate> {
        val resultSet = hashSetOf<Coordinate>()
        for(y in grid.indices) {
            for(x in grid.first().indices) {
                if(grid[y][x] == '#') resultSet.add(Coordinate(x.toLong(), y.toLong()))
            }
        }
        return resultSet
    }

    private fun findGalaxyPairs(galaxyLocations: Set<Coordinate>, rowExpansions: Set<Int>, columnExpansions: Set<Int>, expansionFactor: Int): Set<GalaxyPair> {
        val pairs = HashSet<GalaxyPair>()
        galaxyLocations.map { currentGalaxy ->
            val expandedGalaxy = findExpandedGalaxyCoords(currentGalaxy, rowExpansions, columnExpansions, expansionFactor)
            val subset = galaxyLocations.toHashSet().subtract(setOf(currentGalaxy))
            for(otherGalaxy in subset) {
                val expandedOtherGalaxy = findExpandedGalaxyCoords(otherGalaxy, rowExpansions, columnExpansions, expansionFactor)
                pairs.add(GalaxyPair(hashSetOf(expandedGalaxy, expandedOtherGalaxy)))
            }
        }
        return pairs
    }
}

fun findExpandedGalaxyCoords(galaxy: Coordinate, rowExpansions: Set<Int>, columnExpansions: Set<Int>, expansionFactor: Int): Coordinate {
    // we can find the new coord by taking the expansion factor minus 1
    // (cause we don't want to count the original) then multiplying that by the number of expansions we have had
    // up until the point that the current x or y coord is. then add the x or y coord back to it to find the new coord.
    val numRowExpansions = rowExpansions.count { it <= galaxy.y }
    val numColumnExpansions = columnExpansions.count { it <= galaxy.x }
    val newX = galaxy.x + (numColumnExpansions * (expansionFactor - 1))
    val newY = galaxy.y + (numRowExpansions * (expansionFactor - 1))
    return Coordinate(newX, newY)
}

fun calculateManhattanDistance(coord1: Coordinate, coord2: Coordinate): Long {
    return abs(coord1.x - coord2.x) + abs(coord1.y - coord2.y)
}

data class GalaxyPair(
    val galaxySet: HashSet<Coordinate>,
    var distance: Long = 0
) {
    init {
        this.distance = calculateManhattanDistance(galaxySet.first(), galaxySet.last())
    }
}

data class Coordinate(
    val x: Long,
    val y: Long
)

fun main() {
    println("Part 1 example solution is: ${Day11.part1("/day11_example.txt")}")
    println("Part 1 main solution is: ${Day11.part1("/day11.txt")}")
    println("Part 2 example solution is: ${Day11.part2("/day11_example.txt")}")
    println("Part 2 main solution is: ${Day11.part2("/day11.txt")}")
}