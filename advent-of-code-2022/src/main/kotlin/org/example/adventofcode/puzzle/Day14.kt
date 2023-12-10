package org.example.adventofcode.puzzle

import org.example.adventofcode.util.FileLoader
import java.lang.IndexOutOfBoundsException

object Day14 {

    const val PRINT_GRID = false

    fun part1(filePath: String): Long {
        val lines = FileLoader.loadFromFile<String>(filePath)
        val sandDropCoord = Coord(500, 0)
        val rockLineCoords = loadRockLineCoords(lines)
        val minMaxCoords = getMaxAndMinCoords(rockLineCoords, sandDropCoord)
        val grid = buildGrid(rockLineCoords, sandDropCoord, minMaxCoords.first, minMaxCoords.second, false)
        return simulateSandFall(grid, sandDropCoord, minMaxCoords.first, minMaxCoords.second)
    }

    fun part2(filePath: String): Long {
        val lines = FileLoader.loadFromFile<String>(filePath)
        val sandDropCoord = Coord(500, 0)
        val rockLineCoords = loadRockLineCoords(lines)
        val minMaxCoords = getMaxAndMinCoords(rockLineCoords, sandDropCoord)
        val grid = buildGrid(rockLineCoords, sandDropCoord, minMaxCoords.first, minMaxCoords.second, true)
        return simulateSandFall(grid, sandDropCoord, minMaxCoords.first, minMaxCoords.second)
    }

    fun simulateSandFall(grid: ArrayList<ArrayList<Char>>, sandDropCoord: Coord, minCoord: Coord, maxCoord: Coord): Long {
        var isFallingIntoAbyss = false
        var sandCount = 0L

        while(!isFallingIntoAbyss) {
            // drop sand
            var isAtRest = false
            var sandPoint = Coord(sandDropCoord.x, sandDropCoord.y)
            grid[sandPoint.y][sandPoint.x] = 'o'
            while(!isAtRest) {
                try {
                    if(grid[sandPoint.y+1][sandPoint.x] != '#' && grid[sandPoint.y+1][sandPoint.x] != 'o') { // can fall down one step
                        grid[sandPoint.y][sandPoint.x] = '.'
                        sandPoint = Coord(sandPoint.x, sandPoint.y+1)
                        grid[sandPoint.y][sandPoint.x] = 'o'
                    } else if(grid[sandPoint.y+1][sandPoint.x-1] != '#' && grid[sandPoint.y+1][sandPoint.x-1] != 'o') { // can fall down left
                        grid[sandPoint.y][sandPoint.x] = '.'
                        sandPoint = Coord(sandPoint.x-1, sandPoint.y+1)
                        grid[sandPoint.y][sandPoint.x] = 'o'
                    } else if(grid[sandPoint.y+1][sandPoint.x+1] != '#' && grid[sandPoint.y+1][sandPoint.x+1] != 'o') { // can fall down right
                        grid[sandPoint.y][sandPoint.x] = '.'
                        sandPoint = Coord(sandPoint.x+1, sandPoint.y+1)
                        grid[sandPoint.y][sandPoint.x] = 'o'
                    } else { // its at rest
                        isAtRest = true
                        sandCount += 1L
                    }

                    if(grid[sandDropCoord.y][sandDropCoord.x] != 'o') {
                        grid[sandDropCoord.y][sandDropCoord.x] = '+'
                    }

                } catch (e: IndexOutOfBoundsException) {
                    isFallingIntoAbyss = true
                    break
                }
            }

            if(isAtRest && !isFallingIntoAbyss && sandPoint.y == 0 && sandPoint.x == 500) { // sand has reached the drop point
                break
            }

        }

        if(PRINT_GRID) {
            printFullGrid(grid, minCoord, maxCoord)
        }
        return sandCount
    }

    fun generateFloorLine(maxCoord: Coord): ArrayList<Coord> {
        return arrayListOf(
            Coord(0, maxCoord.y+2),
            Coord(maxCoord.x+499, maxCoord.y+2)
        )

    }

    fun initializeEmptyGrid(minCoord: Coord, maxCoord: Coord): ArrayList<ArrayList<Char>> {
        val grid = ArrayList<ArrayList<Char>>()
        for(y in 0 until maxCoord.y+3) {
            val line = ArrayList<Char>()
            for (x in 0 until maxCoord.x+500) {
                line.add('.')
            }
            grid.add(line)
        }
        return grid
    }

    fun buildGrid(rockLineCoords: List<List<Coord>>, sandDropCoord: Coord, minCoord: Coord, maxCoord: Coord, shouldDrawFloor: Boolean): ArrayList<ArrayList<Char>> {
        val grid = initializeEmptyGrid(minCoord, maxCoord)
        // Draw Lines
        for(coordList in rockLineCoords) {
            drawLines(coordList, grid)
        }

        // draw floor
        if(shouldDrawFloor) {
            drawLines(generateFloorLine(maxCoord), grid)
        }

        // Set sand drop coord
        grid[sandDropCoord.y][sandDropCoord.x] = '+'

        if(PRINT_GRID) {
            printFullGrid(grid, minCoord, maxCoord)
        }
        return grid
    }

    fun drawLines(coordList: List<Coord>, grid: ArrayList<ArrayList<Char>>) {
        for (i in 0 until coordList.size-1) {
            val firstCord = coordList[i]
            val secondCoord = coordList[i+1]

            // if it moves horizontal
            if(firstCord.y == secondCoord.y && firstCord.x < secondCoord.x) { //horizontal
                for(x in firstCord.x .. secondCoord.x) {
                    grid[firstCord.y][x] = '#'
                }
            } else if(firstCord.y == secondCoord.y && firstCord.x > secondCoord.x) {
                for (x in secondCoord.x .. firstCord.x) {
                    grid[firstCord.y][x] = '#'
                }
            } else if(firstCord.x == secondCoord.x && firstCord.y < secondCoord.y) { //horizontal
                for(y in firstCord.y .. secondCoord.y) {
                    grid[y][firstCord.x] = '#'
                }
            } else if(firstCord.x == secondCoord.x && firstCord.y > secondCoord.y) {
                for (y in secondCoord.y .. firstCord.y) {
                    grid[y][firstCord.x] = '#'
                }
            }
        }
    }

    fun printGrid(grid: List<List<Char>>, minCoord: Coord, maxCoord: Coord) {
        print("\n\n")
        for (y in grid.indices) {
            for (x in grid[y].indices) {
                if(x >= minCoord.x && x <= maxCoord.x) print(grid[y][x])
            }
            if(y >= minCoord.y && y <= maxCoord.y+2) print("\n")
        }
        print("\n\n")
    }

    fun printFullGrid(grid: List<List<Char>>, minCoord: Coord, maxCoord: Coord) {
        print("\n\n")
        for (y in grid.indices) {
            for (x in grid[y].indices) {
                print(grid[y][x])
            }
            print("\n")
        }
        print("\n\n")
    }

    fun getMaxAndMinCoords(rockLineCoords: List<List<Coord>>, sandDropCoord: Coord): Pair<Coord, Coord> {
        val maxCoord = Coord(0,0)
        val minCoord = Coord(100_000, 100_000)
        for (line in rockLineCoords) {
            for (coord in line) {
                if(coord.x > maxCoord.x) {
                    maxCoord.x = coord.x
                }
                if(coord.y > maxCoord.y) {
                    maxCoord.y = coord.y
                }
                if(coord.x < minCoord.x) {
                    minCoord.x = coord.x
                }
                if(coord.y < minCoord.y) {
                    minCoord.y = coord.y
                }
            }
        }

        if (sandDropCoord.x > maxCoord.x) {
            maxCoord.x = sandDropCoord.x
        }

        if (sandDropCoord.y > maxCoord.y) {
            maxCoord.y = sandDropCoord.y
        }

        if (sandDropCoord.x < minCoord.x) {
            minCoord.x = sandDropCoord.x
        }

        if (sandDropCoord.y < minCoord.y) {
            minCoord.y = sandDropCoord.y
        }

        return Pair(minCoord, maxCoord)
    }


    // Loader for array of array of coords?
    fun loadRockLineCoords(lines: List<String>): ArrayList<ArrayList<Coord>> {
        val rockLines = ArrayList<ArrayList<Coord>>()
        for (line in lines) {
            val coordList = ArrayList<Coord>()
            val parts = line.split("->")
            for (part in parts) {
                val coordString = part.split(",")
                coordList.add(Coord(coordString[0].trim().toInt(), coordString[1].trim().toInt()))
            }
            rockLines.add(coordList)
        }
        return rockLines
    }


    // Coordinates Class
    data class Coord(
        var x: Int,
        var y: Int
    )
}

fun main() {
    println("Part 1 example solution is: ${Day14.part1("/day14_example.txt")}")
    println("Part 1 main solution is: ${Day14.part1("/day14.txt")}")
    println("Part 2 example solution is: ${Day14.part2("/day14_example.txt")}")
    println("Part 2 main solution is: ${Day14.part2("/day14.txt")}")
}