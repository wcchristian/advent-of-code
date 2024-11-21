package org.example.adventofcode.puzzle

import org.example.adventofcode.util.Utils
import kotlin.math.pow

object Day04 {
    fun part1(filePath: String): Long {
        val fileLines = Utils.loadFromFile<String>(filePath)
        return fileLines.map {
            parseCard(it)
        }.sumOf(Card::calculatePoints)
    }

    fun part2(filePath: String): Long {
        val fileLines = Utils.loadFromFile<String>(filePath)
        val cards = fileLines.map {
            parseCard(it)
        }
        return cards.sumOf { processCard(it, cards) }
    }

    private fun processCard(currentCard: Card, fullCardList: List<Card>): Long {
        return if(currentCard.findMatchCount() == 0) {
            1 // if there are no matches, ONLY count the current card
        } else {
            fullCardList.subList(currentCard.cardId, currentCard.cardId + currentCard.findMatchCount()).sumOf {
                processCard(it, fullCardList)
            } + 1 // If there are matches, count the current card (+1) AND recur to process each matched card
        }
    }

    private fun parseCard(line: String): Card {
        val cardSplit = line.split(":")
        val numberSplit = cardSplit[1].split("|")
        val cardId = Regex("Card\\s+(\\d+)").find(cardSplit[0])!!.groupValues[1].toInt()
        val winningNumbers = Regex("\\s*(\\d+)\\s*").findAll(numberSplit[0].trim()).map { it.value.trim().toInt() }.toList()
        val cardNumbers = Regex("\\s*(\\d+)\\s*").findAll(numberSplit[1].trim()).map { it.value.trim().toInt() }.toList()
        return Card(cardId, winningNumbers, cardNumbers)

    }
}

data class Card(
    val cardId: Int,
    val winningNumbers: List<Int>,
    val cardNumbers: List<Int>
) {
    fun calculatePoints(): Long {
        var matches = 0
        this.cardNumbers.forEach { number ->
            if(this.winningNumbers.contains(number)) {
                matches++
            }
        }
        return if(matches > 0) 2.0.pow((matches - 1).toDouble()).toLong() else 0
    }

    fun findMatchCount(): Int {
        return this.cardNumbers.filter { this.winningNumbers.contains(it) }.size
    }
}

fun main() {
    println("Part 1 example solution is: ${Day04.part1("/day04_example.txt")}")
    println("Part 1 main solution is: ${Day04.part1("/day04.txt")}")
    println("Part 2 example solution is: ${Day04.part2("/day04_example.txt")}")
    println("Part 2 main solution is: ${Day04.part2("/day04.txt")}")
}