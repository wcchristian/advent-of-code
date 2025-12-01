use std::fs;
use std::path::Path;

fn main() {
    let filename = "day01_input.txt";
    let example_filename = "day01_example.txt";

    println!("Part 1 Example: {}", part1(example_filename));
    println!("Part 1: {}", part1(filename));
    println!("Part 2 Example: {}", part2(example_filename));
    println!("Part 2: {}", part2(filename));
}

fn part1(filename: &str) -> i32 {
    let lines = read_file(filename);
    let mut position = 50;
    let mut counter = 0;

    for line in lines {
        let direction = line.chars().next().unwrap();
        let distance: i32 = line[1..].parse().unwrap();

        if direction == 'R' {
            position += distance;
        } else if direction == 'L' {
            position -= distance;
        }

        position = position.rem_euclid(100);

        if position == 0 {
            counter += 1;
        }
    }

    return counter
}

fn part2(filename: &str) -> i32 {
    let mut position = 50;
    let mut counter = 0;
    let lines = read_file(filename);

    for line in lines {
        let starting_pos = position;
        let direction = line.chars().next().unwrap();
        let full_distance: i32 = line[1..].parse().unwrap();
        let distance = full_distance % 100;
        counter += full_distance / 100;

        if direction == 'R' && position + distance > 99 {
            position = (position + distance) - 100;
            counter += if starting_pos != 0 { 1 } else { 0 };
        } else if direction == 'R' {
            position += distance;
            counter += if position == 0 { 1 } else { 0 };
        } else if direction == 'L' && position - distance < 0 {
            position = 100 - (position - distance).abs();
            counter += if starting_pos != 0 { 1 } else { 0 };
        } else if direction == 'L' {
            position -= distance;
            counter += if position == 0 { 1 } else { 0 };
        }
    }

    return counter
}

fn read_file(filename: &str) -> Vec<String> {
    let path = Path::new(file!()).parent().unwrap().join(filename);
    let contents = fs::read_to_string(path).expect("Failed to read file");
    contents
        .trim()
        .lines()
        .map(|s| s.to_string())
        .collect()
}