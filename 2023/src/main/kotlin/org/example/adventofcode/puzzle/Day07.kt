package org.example.adventofcode.puzzle

import org.example.adventofcode.util.FileLoader

object Day07 {
    fun part1(filePath: String): Int {
        val fileLines = FileLoader.loadFromFile<String>(filePath)
        return parseHands(fileLines).sortedWith(compareBy<Hand> { hand ->
            hand.handType.value
        }.then(getTieBreakComparator(cardValueMap))).mapIndexed { i, hand ->
            hand.wager  * (i + 1)
        }.sumOf { it }
    }

    fun part2(filePath: String): Int {
        val fileLines = FileLoader.loadFromFile<String>(filePath)
        val idk =  parseHands(fileLines)
        return idk.sortedWith(compareBy<Hand> { hand ->
            hand.jokerHandType.value
        }.then(getTieBreakComparator(jokerCardValueMap))).mapIndexed { i, hand ->
            hand.wager  * (i + 1)
        }.sumOf { it }
    }

    private fun parseHands(fileLines: List<String>) = fileLines.map { line ->
        val (cards, wager) = line.split(" ")
        val cardMap = mutableMapOf<Char, Int>()
        cards.toCharArray().forEach { char ->
            cardMap[char] = (cardMap[char] ?: 0) + 1
        }
        val sortedCardList = cardMap.toList().sortedWith(compareBy({it.second}, {cardValueMap[it.first]})).reversed()
        val jokerMap = sortedCardList.associateBy({it.first}, {it.second}).toMutableMap()

        if(cards == "JJJJJ") {
            jokerMap['A'] = 5
        } else if(sortedCardList.first().first == 'J') { // If joker is the high card
            jokerMap[jokerMap.keys.toList()[1]] = jokerMap[jokerMap.keys.toList()[1]]!! + (jokerMap['J'] ?: 0)
        } else {
            jokerMap[jokerMap.keys.first()] = jokerMap[jokerMap.keys.first()]!! + (jokerMap['J'] ?: 0)
        }
        jokerMap.remove('J')

        Hand(
            cards,
            sortedCardList.toMap(),
            jokerMap,
            wager.toInt(),
            evalHandType(sortedCardList.toMap()),
            evalHandType(jokerMap)
        )
    }

    private fun evalHandType(cardMap: Map<Char, Int>): HandType {
        if(cardMap.values.any { it == 5 }) return HandType.FIVE_OF_A_KIND
        if(cardMap.values.any { it == 4 }) return HandType.FOUR_OF_A_KIND
        if(cardMap.values.any { it == 2 } && cardMap.values.any { it == 3 }) return HandType.FULL_HOUSE
        if(cardMap.values.any { it == 3 }) return HandType.THREE_OF_A_KIND
        if(cardMap.values.count { it == 2 } == 2) return HandType.TWO_PAIR
        if(cardMap.values.any { it == 2 }) return HandType.PAIR
        return HandType.HIGH_CARD
    }
}


data class Hand(
    val cardString: String,
    val cardMap: Map<Char, Int>,
    val jokerCardMap: Map<Char, Int>,
    val wager: Int,
    var handType: HandType = HandType.HIGH_CARD,
    val jokerHandType: HandType = HandType.HIGH_CARD
)

val cardValueMap = mapOf(
    '2' to 2,
    '3' to 3,
    '4' to 4,
    '5' to 5,
    '6' to 6,
    '7' to 7,
    '8' to 8,
    '9' to 9,
    'T' to 10,
    'J' to 11,
    'Q' to 12,
    'K' to 13,
    'A' to 14
)

val jokerCardValueMap = cardValueMap.toMutableMap().apply {
    this['J'] = 1
}.toMap()

enum class HandType(val value: Int) {
    HIGH_CARD(1),
    PAIR(2),
    TWO_PAIR(3),
    THREE_OF_A_KIND(4),
    FULL_HOUSE(5),
    FOUR_OF_A_KIND(6),
    FIVE_OF_A_KIND(7)
}

fun getTieBreakComparator(valueMap: Map<Char, Int>) = Comparator<Hand> { hand1, hand2 ->
    if(hand1.cardString.length == hand2.cardString.length) {
        var result = 0
        for (char in hand1.cardString.indices) {
            val o1Val = valueMap[hand1.cardString[char]] ?: 0
            val o2Val = valueMap[hand2.cardString[char]] ?: 0
            if (o1Val != o2Val) {
                result = o1Val.compareTo(o2Val)
                break
            }
        }
        result
    } else {
        println("Uh Oh, this wasn't supposed to be possible")
        0
    }
}

fun main() {
    println("Part 1 example solution is: ${Day07.part1("/day07_example.txt")}")
    println("Part 1 main solution is: ${Day07.part1("/day07.txt")}")
    println("Part 2 example solution is: ${Day07.part2("/day07_example.txt")}")
    println("Part 2 main solution is: ${Day07.part2("/day07.txt")}")
}