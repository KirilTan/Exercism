int ovenTime() {
    return 40;
}

/* remainingOvenTime returns the remaining
   minutes based on the actual minutes already in the oven.
*/
int remainingOvenTime(const int actualMinutesInOven) {
    const int total_time {ovenTime()};

    return total_time - actualMinutesInOven;
}

/* preparationTime returns an estimate of the preparation time based on the
   number of layers and the necessary time per layer.
*/
int preparationTime(const int numberOfLayers, const int timePerLayer = 2) {
    return numberOfLayers * timePerLayer;
}

// elapsedTime calculates the total time spent to create and bake the lasagna so
// far.
int elapsedTime(const int numberOfLayers, const int actualMinutesInOven) {
    return actualMinutesInOven + preparationTime(numberOfLayers);
}
