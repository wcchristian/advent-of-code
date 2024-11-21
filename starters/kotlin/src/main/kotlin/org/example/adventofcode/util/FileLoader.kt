package org.example.adventofcode.util

import java.util.stream.Collectors

@Suppress("UNCHECKED_CAST")
object FileLoader {

    inline fun <reified T> loadFromFile(filePath: String): List<T> {
        val fileText = FileLoader::class.java.getResource(filePath)!!.readText() // Just NPE if file can't be found
        return when(T::class) { // Add cases below as you need to extend for specific puzzles.
            Int::class -> fileText.lines().stream().map { it.toInt() }.collect(Collectors.toList()) as List<T>
            Float::class -> fileText.lines().stream().map { it.toFloat() }.collect(Collectors.toList()) as List<T>
            String::class -> fileText.lines() as List<T>
            else -> fileText.lines() as List<T> // Default is treated like strings
        }
    }
}