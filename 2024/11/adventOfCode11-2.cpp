#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <unordered_map>

#define MAX_ROCKS 1000
#define MAX_LENGTH 100

std::string addToKeyValueArray(std::unordered_map<std::string, std::string> &results, const std::string &key, const std::string &value) {
    auto it = results.find(key);
    if (it != results.end()) {
        return it->second;
    }
    results[key] = value;
    return results[key];
}

void numberOfRock(std::string &rocks, int blink, std::unordered_map<std::string, std::string> &results, int &rockCount) {
    int blinkCounter = 0;
    while (blinkCounter <= blink) {
        std::string tempRocks;
        std::istringstream iss(rocks);
        std::string rock;
        while (iss >> rock) {
            bool rockDone = false;
            auto it = results.find(rock);
            if (it != results.end()) {
                tempRocks += " " + it->second;
                rockDone = true;
            }
            if (rock.length() % 2 == 0 && !rockDone) {
                int value = std::stoi(rock) / 2;
                std::string newNumer = std::to_string(value) + " " + std::to_string(value);
                tempRocks += " " + newNumer;
                addToKeyValueArray(results, rock, newNumer);
                rockDone = true;
            } else if (!rockDone) {
                std::string newNumer = std::to_string(std::stoi(rock) * 2024);
                tempRocks += " " + newNumer;
                addToKeyValueArray(results, rock, newNumer);
            }
        }
        blinkCounter++;
        rocks = tempRocks.substr(1); // Skip the leading space
    }
    rockCount = !rocks.empty() ? std::count(rocks.begin(), rocks.end(), ' ') + 1 : 0;
}

int main() {
    std::string rocksLine = "1 2 3 4 5"; // Placeholder for file content
    std::unordered_map<std::string, std::string> results = {{"0", "1"}};
    int blinkNeeded = 25;
    int nbRocks = 0;
    int counter = 1;

    std::cout << "Starting...\n";

    std::istringstream iss(rocksLine);
    std::string singleRock;
    while (iss >> singleRock) {
        int nbRocksForRun = 0;
        numberOfRock(singleRock, blinkNeeded, results, nbRocksForRun);
        nbRocks += nbRocksForRun;
        counter++;
        std::cout << counter << "/" << (std::count(rocksLine.begin(), rocksLine.end(), ' ') + 1) << "\n";
    }

    std::cout << "Number of blink: " << blinkNeeded << "\n";
    std::cout << "number of rocks: " << nbRocks << "\n";
    std::cout << "expected result:  183435\n";

    return 0;
}