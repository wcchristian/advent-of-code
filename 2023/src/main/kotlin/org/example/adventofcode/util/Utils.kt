package org.example.adventofcode.util

import java.util.stream.Collectors

@Suppress("UNCHECKED_CAST")
object Utils {

    inline fun <reified T> loadFromFile(filePath: String): List<T> {
        val fileText = Utils::class.java.getResource(filePath)!!.readText() // Just NPE if file can't be found
        return when(T::class) { // Add cases below as you need to extend for specific puzzles.
            Int::class -> fileText.lines().stream().map { it.toInt() }.collect(Collectors.toList()) as List<T>
            Float::class -> fileText.lines().stream().map { it.toFloat() }.collect(Collectors.toList()) as List<T>
            String::class -> fileText.lines() as List<T>
            else -> fileText.lines() as List<T> // Default is treated like strings
        }
    }

    fun loadCharGridFromFile(filePath: String): CharGrid {
        val fileLines = loadFromFile<String>(filePath)
        val grid = mutableListOf<MutableList<Char>>()
        fileLines.forEachIndexed { yIdx, string ->
            val row = string.toMutableList()
            grid.add(row)
        }
        return grid
    }

}

typealias CharGrid = MutableList<MutableList<Char>>

fun CharGrid.stringify(delimiter: String = ""): String {
    var string = ""
    for(y in this.indices) {
        for(x in this.first().indices) {
            string += this[y][x] + delimiter
        }
        string += "\n"
    }
    return string
}

fun CharGrid.print() {
    print(this.stringify())
}

fun CharGrid.copy(): CharGrid {
    return ArrayList(this.map { it.map { it }.toMutableList() })
}