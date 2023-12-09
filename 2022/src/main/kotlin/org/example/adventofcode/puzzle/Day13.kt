package org.example.adventofcode.puzzle

import org.example.adventofcode.util.FileLoader
import java.lang.IndexOutOfBoundsException
import java.lang.NumberFormatException

object Day13 {

    fun part1(filePath: String): Int {
        val lines = FileLoader.loadFromFile<String>(filePath)
        val pairs = loadPacketPairs(lines)
        val correctOrderIndices = ArrayList<Int>()

        for (pairIdx in pairs.indices) {
            val isCorrectOrder = isCorrectOrder(pairs[pairIdx][0], pairs[pairIdx][1])
            if(isCorrectOrder == -1) {
                correctOrderIndices.add(pairIdx+1)
            }
        }
        return correctOrderIndices.sum()
    }

    fun part2(filePath: String): Int {
        val lines = FileLoader.loadFromFile<String>(filePath)
        val pairs = loadPacketList(lines)

        //Add divider packets
        pairs.add("[[2]]")
        pairs.add("[[6]]")

        val sortedPackets = pairs.sortedWith { a, b ->
            isCorrectOrder(a, b)
        }

        val dividerPacketIndexes = ArrayList<Int>()
        for (i in sortedPackets.indices) {
            if(sortedPackets[i] == "[[2]]" || sortedPackets[i]  == "[[6]]") {
                dividerPacketIndexes.add(i+1)
            }
        }

        return dividerPacketIndexes[0] * dividerPacketIndexes[1]
    }

    /**
     * Returns -1 if they are in the right order, 1 if in the wrong order, 0 if no decision
     */
    fun isCorrectOrder(left: String, right: String): Int {
        val leftElems = left.sanitizeAndSplit(',')
        val rightElems = right.sanitizeAndSplit(',')
        var isCorrectOrder = 0

        try {
            for(i in leftElems.indices) {
                if (leftElems[i].isIntParseable() && rightElems[i].isIntParseable()) { // int and int
                    isCorrectOrder = compareInts(leftElems[i].toInt(), rightElems[i].toInt())
                } else if (leftElems[i].isList() && rightElems[i].isList()) { // list and list
                    isCorrectOrder = isCorrectOrder(leftElems[i], rightElems[i])
                } else if (leftElems[i].isIntParseable() && rightElems[i].isList()) { // int and list
                    isCorrectOrder = isCorrectOrder("[${leftElems[i]}]", rightElems[i])
                } else if (leftElems[i].isList() && rightElems[i].isIntParseable()) { // list and int
                    isCorrectOrder = isCorrectOrder(leftElems[i], "[${rightElems[i]}]")
                }

                if(isCorrectOrder != 0) { // escape the loop if we have a decision
                    break
                }
            }
        } catch(e: IndexOutOfBoundsException) { // If index is out of bounds, then we know that right has less elements than left and they are out of order.
            isCorrectOrder = 1
        }


        // If no decision check list lengths
        if(isCorrectOrder == 0 && leftElems.size < rightElems.size) {
            isCorrectOrder = -1
        } else if(isCorrectOrder == 0 && rightElems.size < leftElems.size) {
            isCorrectOrder = 1 // due to the try catch above, this is probably not needed
        }

        return isCorrectOrder
    }

    fun compareInts(left: Int, right: Int): Int {
        if (left < right) {
            return -1
        } else if (right < left) {
            return 1
        } else {
            return 0
        }
    }

    fun String.sanitizeAndSplit(splitChar: Char): List<String> {
        val splitList = ArrayList<String>()
        var bracketDepth = 0
        var resultString = ""
        val tmpString = this.removePrefix("[").removeSuffix("]")

        for(char in tmpString) {
            if(char == splitChar && bracketDepth == 0) {
                splitList.add(resultString)
                resultString = String()
            } else if(char == '[') {
                bracketDepth += 1
                resultString += char
            } else if(char == ']') {
                bracketDepth -= 1
                resultString += char
            } else {
                resultString += char
            }
        }

        if(resultString.isNotBlank()) {
            splitList.add(resultString)
        }
        return splitList
    }

    fun String.isIntParseable(): Boolean {
        return try {
            this.toInt()
            true
        } catch (e: NumberFormatException) {
            false
        }
    }

    fun String.isList(): Boolean {
        return this.startsWith("[") && this.endsWith("]")
    }

    fun loadPacketPairs(lines: List<String>): List<List<String>> {
        val pairs = ArrayList<ArrayList<String>>()
        var packets = ArrayList<String>()
        for (line in lines) {
            if(line.isNotBlank()) {
                packets.add(line)
            } else {
                pairs.add(packets)
                packets = ArrayList<String>()
            }
        }
        pairs.add(packets)
        return pairs
    }

    fun loadPacketList(lines: List<String>): ArrayList<String> {
        val packetList = ArrayList<String>()
        for (line in lines) {
            if(line.isNotBlank()) {
                packetList.add(line)
            }
        }
        return packetList
    }
}

fun main() {
    println("Part 1 example solution is: ${Day13.part1("/day13_example.txt")}")
    println("Part 1 main solution is: ${Day13.part1("/day13.txt")}")
    println("Part 2 example solution is: ${Day13.part2("/day13_example.txt")}")
    println("Part 2 main solution is: ${Day13.part2("/day13.txt")}")
}