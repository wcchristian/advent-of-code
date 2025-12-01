use std::fs;
use std::path::Path;

fn main() {
    let filename = "day00_input.txt";
    let example_filename = "day00_example.txt";

    println!("Part 1 Example: {}", part1(example_filename));
    println!("Part 1: {}", part1(filename));
    println!("Part 2 Example: {}", part2(example_filename));
    println!("Part 2: {}", part2(filename));
}

fn part1(filename: &str) -> i32 {
    return 0;
}

fn part2(filename: &str) -> i32 {
    return 0;
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