package org.example.adventofcode.puzzle

import org.example.adventofcode.util.Utils

object Day03 {
    fun part1(filePath: String): Int {
        val fileLines = Utils.loadFromFile<String>(filePath)

        val potentialPartNumbers = arrayListOf<PartNumber>()
        fileLines.forEachIndexed { y, line ->
            var currentPotentialPartNumber = PartNumber("", arrayListOf())
            line.forEachIndexed { x, char ->
                if(char.isDigit()) {
                    currentPotentialPartNumber.number += char
                    currentPotentialPartNumber.numberCoords.add(Coord(x=x, y=y))
                } else {
                    if(currentPotentialPartNumber.number.isNotBlank()) {
                        potentialPartNumbers.add(currentPotentialPartNumber)
                    }
                    currentPotentialPartNumber = PartNumber("", arrayListOf())
                }
            }
            potentialPartNumbers.add(currentPotentialPartNumber)
        }

        return potentialPartNumbers
            .filter { isValidPartNumber(it, fileLines) }
            .sumOf { it.number.toInt() }
    }

    fun part2(filePath: String): Int {
        val fileLines = Utils.loadFromFile<String>(filePath)
        return fileLines.mapIndexed { y, line ->
            line.mapIndexed { x, char ->
                if(char == '*') Coord(x, y) else null
            }
        }.flatten().filterNotNull().map {
            findConnectedParts(it.x, it.y, fileLines)
        }.filter { it.isNotEmpty() }.sumOf {
            it.map { it.number.toInt() }.reduce {acc, partNumber -> acc * partNumber}
        }
    }

    private fun findConnectedParts(x: Int, y: Int, map: List<String>): HashSet<PartNumber> {
        val partsList = arrayListOf<PartNumber>()
        if (y - 1 >= 0 && x-1 >= 0 && map[y-1][x-1].isDigit()) partsList.add(buildNumberFromPoint(x-1, y-1, map))
        if (y - 1 >= 0 && map[y-1][x].isDigit()) partsList.add(buildNumberFromPoint(x, y-1, map))
        if (y - 1 >= 0 && x+1 < map.first().length && map[y-1][x+1].isDigit()) partsList.add(buildNumberFromPoint(x+1, y-1, map))

        if (x - 1 >= 0 && map[y][x-1].isDigit()) partsList.add(buildNumberFromPoint(x-1, y, map))
        if (x + 1 < map.first().length && map[y][x+1].isDigit()) partsList.add(buildNumberFromPoint(x+1, y, map))

        if (y + 1 < map.size && x-1 >= 0 && map[y+1][x-1].isDigit()) partsList.add(buildNumberFromPoint(x-1, y+1, map))
        if (y + 1 < map.size && map[y+1][x].isDigit()) partsList.add(buildNumberFromPoint(x, y+1, map))
        if (y + 1 < map.size && x+1 < map.first().length && map[y+1][x+1].isDigit()) partsList.add(buildNumberFromPoint(x+1, y+1, map))

        return if(partsList.toHashSet().size == 2) partsList.toHashSet() else hashSetOf()
    }

    private fun buildNumberFromPoint(x: Int, y:Int, map: List<String>): PartNumber {
        val partNumber = PartNumber(map[y][x].toString(), arrayListOf(Coord(x, y)))
        val currentLine = map[y]

        for (i in x+1 ..< currentLine.length) {
            if(currentLine[i].isDigit()) {
                partNumber.number += currentLine[i]
                partNumber.numberCoords.add(Coord(i, y))
            } else {
                break
            }
        }

        for (i in x-1 downTo 0) {
            if(currentLine[i].isDigit()) {
                partNumber.number = currentLine[i].toString()+ partNumber.number
                partNumber.numberCoords.add(Coord(i, y))
            } else {
                break
            }
        }
        return partNumber
    }

    private fun isValidPartNumber(partNumber: PartNumber, map: List<String>): Boolean {
        partNumber.numberCoords.forEach {
                if (it.y - 1 >= 0 && it.x-1 >= 0 && map[it.y-1][it.x-1].isSymbol()) return true
                if (it.y - 1 >= 0 && map[it.y-1][it.x].isSymbol()) return true
                if (it.y - 1 >= 0 && it.x+1 < map.first().length && map[it.y-1][it.x+1].isSymbol()) return true

                if (it.x - 1 >= 0 && map[it.y][it.x-1].isSymbol()) return true
                if (it.x + 1 < map.first().length && map[it.y][it.x+1].isSymbol()) return true

                if (it.y + 1 < map.size && it.x-1 >= 0 && map[it.y+1][it.x-1].isSymbol()) return true
                if (it.y + 1 < map.size && map[it.y+1][it.x].isSymbol()) return true
                if (it.y + 1 < map.size && it.x+1 < map.first().length && map[it.y+1][it.x+1].isSymbol()) return true
        }
        return false
    }
}

fun Char.isSymbol(): Boolean {
    return !this.isLetterOrDigit() && this != '.'
}

data class Coord(
    val x: Int,
    val y: Int
) {
    override fun hashCode(): Int {
        return x.hashCode() + y.hashCode()
    }

    override fun equals(other: Any?): Boolean {
        if (this === other) return true
        if (other !is Coord) return false
        if(this.x != other.x) return false
        if(this.y != other.y) return false
        return true
    }
}

data class PartNumber(
    var number: String,
    val numberCoords: ArrayList<Coord>
) {
    override fun hashCode(): Int {
        return number.hashCode() + numberCoords.sortedWith(compareBy({it.x}, {it.y})).hashCode()
    }

    override fun equals(other: Any?): Boolean {
        if(this === other) return true
        if(other !is PartNumber) return false
        if(this.number != other.number) return false
        return this.numberCoords.sortedWith(compareBy({ it.x }, { it.y })).equals(other.numberCoords.sortedWith(
            compareBy({it.x}, {it.y})
        ))
    }
}

fun main() {
    println("Part 1 example solution is: ${Day03.part1("/day03_example.txt")}")
    println("Part 1 main solution is: ${Day03.part1("/day03.txt")}")
    println("Part 2 example solution is: ${Day03.part2("/day03_example.txt")}")
    println("Part 2 main solution is: ${Day03.part2("/day03.txt")}")
}