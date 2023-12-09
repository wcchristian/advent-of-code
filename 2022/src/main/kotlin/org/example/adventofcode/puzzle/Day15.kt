package org.example.adventofcode.puzzle

import org.example.adventofcode.util.FileLoader
import java.lang.Integer.max
import java.lang.Integer.sum
import java.util.*
import java.util.stream.Collectors
import kotlin.collections.ArrayList
import kotlin.collections.HashSet
import kotlin.math.abs

object Day15 {

    fun part1(filePath: String, rowToCheck: Int): Int {
        val lines = FileLoader.loadFromFile<String>(filePath)
        val sensorList = loadSensors(lines)
        val coordNotPossibleOnTargetRow = HashSet<Int>()
        val sensorsExistOnRowToCheck = sensorList.stream().filter {
            it.beaconCoord.y == rowToCheck
        }.map {
            it.beaconCoord.x
        }.collect(Collectors.toSet())

        for (sensor in sensorList) {
            val manhattanDistance = findManhattanDistance(sensor.sensorCoord, sensor.beaconCoord)
            val up = sensor.sensorCoord.y - manhattanDistance
            val down = sensor.sensorCoord.y + manhattanDistance

            if(rowToCheck in up..down) {
                // if greater than the sensor
                var distance = 0
                if(rowToCheck > sensor.sensorCoord.y) {
                    distance = abs(down - rowToCheck)
                } else if(rowToCheck < sensor.sensorCoord.y) {
                    distance = abs(up - rowToCheck)
                }
                for (i in 0 .. distance) {
                    // if not one of the spots where a sensor exists
                    if(!sensorsExistOnRowToCheck.contains(sensor.sensorCoord.x-i)) {
                        coordNotPossibleOnTargetRow.add(sensor.sensorCoord.x-i)
                    }

                    if(!sensorsExistOnRowToCheck.contains(sensor.sensorCoord.x+i)) {
                        coordNotPossibleOnTargetRow.add(sensor.sensorCoord.x+i)
                    }
                }
            }
        }

        return coordNotPossibleOnTargetRow.size
    }

    fun part2(filePath: String, maxSize: Int): Int {
        val lines = FileLoader.loadFromFile<String>(filePath)
        return 1
    }

    fun findManhattanDistance(point1: Coord, point2: Coord): Int {
        return sum(abs(point1.x - point2.x), abs(point1.y - point2.y))
    }

    fun loadSensors(lines: List<String>): List<Sensor> {
        val sensorList = ArrayList<Sensor>()
        for (line in lines) {
            val lineParts = line.split(":")
            val sensorCoordSplit = lineParts[0].removePrefix("Sensor at ").split(",")
            val beaconCoordSplit = lineParts[1].removePrefix(" closest beacon is at ").split(",")
            sensorList.add(
                Sensor(
                    Coord(sensorCoordSplit[0].removePrefix("x=").trim().toInt(), sensorCoordSplit[1].removePrefix(" y=").trim().toInt()),
                    Coord(beaconCoordSplit[0].removePrefix("x=").trim().toInt(), beaconCoordSplit[1].removePrefix(" y=").trim().toInt())
                )
            )
        }

        return sensorList
    }

    data class Coord(
        val x: Int,
        val y: Int
    ) {
        override fun hashCode(): Int {
            return Objects.hash(x, y)
        }

        override fun equals(other: Any?): Boolean {
            if (this === other) return true
            if (javaClass != other?.javaClass) return false

            other as Coord

            if (x != other.x) return false
            if (y != other.y) return false

            return true
        }
    }

    data class Sensor(
        val sensorCoord: Coord,
        val beaconCoord: Coord
    )
}

fun main() {
    println("Part 1 example solution is: ${Day15.part1("/day15_example.txt", 10)}")
    println("Part 1 main solution is: ${Day15.part1("/day15.txt", 2_000_000)}")
    println("Part 2 example solution is: ${Day15.part2("/day15_example.txt", 20)}")
    println("Part 2 main solution is: ${Day15.part2("/day15.txt", 4_000_000)}")
}