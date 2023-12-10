package org.example.adventofcode.puzzle

import org.example.adventofcode.util.FileLoader

object Day05 {
    fun part1(filePath: String): Long {
        val fileLines = FileLoader.loadFromFile<String>(filePath)
        val almanac = parseInput(fileLines)
        return processSeeds(almanac).minOf { it.locationNumber }
    }

    fun part2(filePath: String): Long {
        val fileLines = FileLoader.loadFromFile<String>(filePath)
        val almanac = parseInput(fileLines)

        var locationNumberToCheck = 0L
        var locationFound = false
        while(!locationFound) {
            val seedToCheck = lookupSeedFromLocation(locationNumberToCheck, almanac)
            for(range in almanac.seedRangeList) {
                val seedOffset = seedToCheck - range.first
                if(seedOffset > 0 && seedOffset < range.second) {
                    locationFound = true
                    break
                }
            }
            if(!locationFound) locationNumberToCheck++
        }

        return locationNumberToCheck
    }

    private fun lookupSeedFromLocation(location: Long, almanac: Almanac): Long {
        val humidityNumber = almanac.lookups.find { it.source == Type.HUMIDITY && it.destination == Type.LOCATION }!!.findSource(location)
        val temperatureNumber = almanac.lookups.find { it.source == Type.TEMPERATURE && it.destination == Type.HUMIDITY }!!.findSource(humidityNumber)
        val lightNumber = almanac.lookups.find { it.source == Type.LIGHT && it.destination == Type.TEMPERATURE }!!.findSource(temperatureNumber)
        val waterNumber = almanac.lookups.find { it.source == Type.WATER && it.destination == Type.LIGHT }!!.findSource(lightNumber)
        val fertilizerNumber = almanac.lookups.find { it.source == Type.FERTILIZER && it.destination == Type.WATER }!!.findSource(waterNumber)
        val soilNumber = almanac.lookups.find { it.source == Type.SOIL && it.destination == Type.FERTILIZER }!!.findSource(fertilizerNumber)
        return almanac.lookups.find { it.source == Type.SEED && it.destination == Type.SOIL }!!.findSource(soilNumber)
    }

    private fun processSeeds(almanac: Almanac): List<Seed> {
        return almanac.seedNumberList.map { seed ->
            val soilNumber = almanac.lookups.find { it.source == Type.SEED && it.destination == Type.SOIL }!!.findDestination(seed)
            val fertilizerNumber = almanac.lookups.find { it.source == Type.SOIL && it.destination == Type.FERTILIZER }!!.findDestination(soilNumber)
            val waterNumber = almanac.lookups.find { it.source == Type.FERTILIZER && it.destination == Type.WATER }!!.findDestination(fertilizerNumber)
            val lightNumber = almanac.lookups.find { it.source == Type.WATER && it.destination == Type.LIGHT }!!.findDestination(waterNumber)
            val temperatureNumber = almanac.lookups.find { it.source == Type.LIGHT && it.destination == Type.TEMPERATURE }!!.findDestination(lightNumber)
            val humidityNumber = almanac.lookups.find { it.source == Type.TEMPERATURE && it.destination == Type.HUMIDITY }!!.findDestination(temperatureNumber)
            val locationNumber = almanac.lookups.find { it.source == Type.HUMIDITY && it.destination == Type.LOCATION }!!.findDestination(humidityNumber)
            Seed(seed, soilNumber, fertilizerNumber, waterNumber, lightNumber, temperatureNumber, humidityNumber, locationNumber)
        }
    }

    private fun parseInput(fileLines: List<String>): Almanac {
        val seedNumberList = fileLines[0].split(":")[1].trim().split(" ").map { it.toLong() }

        val seedString = fileLines[0].split(":")[1].trim()
        val seedNumberPairs = arrayListOf<String>()
        Regex("(\\d+ \\d+)").findAll(seedString).iterator().forEach { seedNumberPairs.add(it.groupValues[1]) }

        val seedRangeList = arrayListOf<Pair<Long, Long>>()
        seedNumberPairs.forEach { pair ->
            val split = pair.split(" ")
            val start = split[0].toLong()
            val range = split[1].toLong()
            seedRangeList.add(Pair(start, range))
        }
        
        val mapChunks = arrayListOf<ArrayList<String>>()
        var currentChunk = arrayListOf<String>()
        fileLines.subList(2, fileLines.size).forEach {
            if(it.isNotBlank()) {
                currentChunk.add(it)
            } else {
                mapChunks.add(currentChunk)
                currentChunk = arrayListOf()
            }
        }
        mapChunks.add(currentChunk) // add the last one.

        val lookups = mapChunks.map { parseChunkToLookup(it) }

        return Almanac(seedNumberList, seedRangeList, lookups)
    }
    
    private fun parseChunkToLookup(chunk: List<String>): Lookup {
        val typeSplit = chunk[0].removeSuffix(" map:").split("-to-")

        val ranges = chunk.subList(1, chunk.size).map { rangeString ->
            val numbers = rangeString.split(" ").map { it.toLong() }
            Range(numbers[0], numbers[1], numbers[2])
        }

        return Lookup(Type.valueOf(typeSplit[0].uppercase()), Type.valueOf(typeSplit[1].uppercase()), ranges)
    }
}

data class Almanac(
    val seedNumberList: List<Long>,
    val seedRangeList: List<Pair<Long, Long>>,
    val lookups: List<Lookup>
)

data class Lookup(
    val source: Type,
    val destination: Type,
    val ranges: List<Range> //TODO: Do I build a map rather than a list of ranges?
) {
    fun findDestination(sourceNumber: Long): Long {
        // build a map of sources to destinations
        for (range in ranges) {
            val sourceOffset = sourceNumber - range.sourceRangeStart
            if(sourceOffset >= 0 && sourceOffset < range.range) {
                return range.destinationRangeStart + sourceOffset
            }
        }
        return sourceNumber
    }

    fun findSource(destinationNumber: Long): Long {
        for (range in ranges) {
            val destinationOffset = destinationNumber - range.destinationRangeStart
            if(destinationOffset >= 0 && destinationOffset < range.range) {
                return range.sourceRangeStart + destinationOffset
            }
        }
        return destinationNumber
    }
}

data class Range(
    val destinationRangeStart: Long,
    val sourceRangeStart: Long,
    val range: Long
)

data class Seed(
    val seedNumber: Long,
    val soilNumber: Long,
    val fertilizerNumber: Long,
    val waterNumber: Long,
    val lightNumber: Long,
    val temperatureNumber: Long,
    val humidityNumber: Long,
    val locationNumber: Long
)

enum class Type {
    SEED,
    SOIL,
    FERTILIZER,
    WATER,
    LIGHT,
    TEMPERATURE,
    HUMIDITY,
    LOCATION
}

fun main() {
    println("Part 1 example solution is: ${Day05.part1("/day05_example.txt")}")
    println("Part 1 main solution is: ${Day05.part1("/day05.txt")}")
    println("Part 2 example solution is: ${Day05.part2("/day05_example.txt")}")
    println("Part 2 main solution is: ${Day05.part2("/day05.txt")}")
}