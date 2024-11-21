package org.example.adventofcode.puzzle

import org.example.adventofcode.util.FileLoader

// A bit long winded today but was tinkering around with kotlin enums and infix functions
object Day02 {
    fun part1(filePath: String): Int {
        val lines = FileLoader.loadFromFile<String>(filePath)
        var score = 0;
        for (line in lines) {
            val lineParts = line.split(" ")
            val opp = RpsChoice fromOpp lineParts[0]
            val self = RpsChoice fromSelf lineParts[1]
            score += getResultScore(self!!, opp!!) + self.choiceScore
        }

        return score
    }

    fun part2(filePath: String): Int {
        val lines = FileLoader.loadFromFile<String>(filePath)
        var score = 0;
        for (line in lines) {
            val lineParts = line.split(" ")
            val opp = RpsChoice fromOpp lineParts[0]
            val expectedResult = Result from lineParts[1]
            val self = getChoice(expectedResult!!, opp!!)
            score += getResultScore(self, opp) + self.choiceScore
        }

        return score
    }

    private fun getResultScore(self: RpsChoice, opponent: RpsChoice): Int {
        if(self == opponent) {
            return 3
        }else if (self == RpsChoice.ROCK && opponent == RpsChoice.SCISSORS
            || self == RpsChoice.SCISSORS && opponent == RpsChoice.PAPER
            || self == RpsChoice.PAPER && opponent == RpsChoice.ROCK) {
            return 6
        } else {
            return 0
        }
    }

    private fun getChoice(result: Result, opponent: RpsChoice): RpsChoice {
        if (result == Result.DRAW) {
            return opponent
        } else if (result == Result.WIN) {
            return RpsChoice findWinner opponent
        } else {
            return RpsChoice findLoser opponent
        }
    }
}

enum class RpsChoice(val opponentKey: String, val selfKey: String, val choiceScore: Int) {
    ROCK("A", "X", 1),
    PAPER("B", "Y", 2),
    SCISSORS("C", "Z", 3);

    companion object {
        private val opponentMap = RpsChoice.values().associateBy { it.opponentKey }
        private val selfMap = RpsChoice.values().associateBy { it.selfKey }
        private val findLoserMap = mapOf(
            ROCK to SCISSORS,
            PAPER to ROCK,
            SCISSORS to PAPER
        )

        infix fun fromOpp(value: String) = opponentMap[value]
        infix fun fromSelf(value: String) = selfMap[value]
        infix fun findLoser(choice: RpsChoice) = findLoserMap[choice]!!
        infix fun findWinner(choice: RpsChoice) = findLoserMap.entries.stream().filter { it.value == choice }.map { it.key }.findFirst().get()
    }
}

enum class Result(val result: String) {
    LOSE("X"),
    DRAW("Y"),
    WIN("Z");

    companion object {
        private val map = Result.values().associateBy { it.result }
        infix fun from(value: String) = map[value]
    }
}

fun main() {
    println("Part 1 example solution is: ${Day02.part1("/day02_example.txt")}")
    println("Part 1 main solution is: ${Day02.part1("/day02.txt")}")
    println("Part 2 example solution is: ${Day02.part2("/day02_example.txt")}")
    println("Part 2 main solution is: ${Day02.part2("/day02.txt")}")
}