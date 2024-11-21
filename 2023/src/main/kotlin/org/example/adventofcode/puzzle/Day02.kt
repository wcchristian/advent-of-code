package org.example.adventofcode.puzzle

import org.example.adventofcode.util.Utils

object Day02 {
    /* ---------- PARTS ---------- */
    fun part1(filePath: String): Int {
        val fileLines = Utils.loadFromFile<String>(filePath)
        return fileLines
            .map { parseGameFromString(it) }
            .filter { isGamePossible(it) }
            .sumOf { it.id }
    }
    fun part2(filePath: String): Int {
        val fileLines = Utils.loadFromFile<String>(filePath)
        return fileLines
            .map { parseGameFromString(it) }
            .map { findMinCubeCountToMakeGamePossible(it) }
            .sumOf { it.blue * it.red * it.green }
    }

    /* ---------- FUNCTIONS ---------- */
    private fun parseGameFromString(line: String): Game {
        return Game(
            id = Regex("Game (\\d*):").find(line)!!.groupValues[1].toInt(),
            cubeCounts = line.split(";").map { handString ->
                CubeCount(
                    blue = Regex("(\\d*) blue").find(handString)?.groupValues?.get(1)?.toInt() ?: 0,
                    red = Regex("(\\d*) red").find(handString)?.groupValues?.get(1)?.toInt() ?: 0,
                    green = Regex("(\\d*) green").find(handString)?.groupValues?.get(1)?.toInt() ?: 0,
                )
            }
        )
    }

    private fun isGamePossible(game: Game): Boolean {
        game.cubeCounts.forEach {
            if(it.blue > 14 || it.green > 13 || it.red > 12) {
                return false
            }
        }
        return true
    }

    private fun findMinCubeCountToMakeGamePossible(game: Game): CubeCount {
        val cubeCount = CubeCount(red = 0, blue = 0, green = 0)
        game.cubeCounts.forEach {
            if (it.red >= cubeCount.red) cubeCount.red = it.red
            if (it.blue >= cubeCount.blue) cubeCount.blue = it.blue
            if (it.green >= cubeCount.green) cubeCount.green = it.green
        }
        return cubeCount
    }

    /* ---------- DATA STRUCTURES ---------- */
    data class Game(
        val id: Int,
        val cubeCounts: List<CubeCount>
    )

    data class CubeCount(
        var blue: Int = 0,
        var red: Int = 0,
        var green: Int = 0
    )
}

/* ---------- MAIN ---------- */
fun main() {
    println("Part 1 example solution is: ${Day02.part1("/day02_example.txt")}")
    println("Part 1 main solution is: ${Day02.part1("/day02.txt")}")
    println("Part 2 example solution is: ${Day02.part2("/day02_example.txt")}")
    println("Part 2 main solution is: ${Day02.part2("/day02.txt")}")
}