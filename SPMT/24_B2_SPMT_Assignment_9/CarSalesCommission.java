public class CarSalesCommission {

    // Method to calculate the commission
    public static double calculateCommission(int numCarsSold, double totalValueSold) {
        // Check for invalid inputs
        if (numCarsSold < 0 || totalValueSold < 0) {
            throw new IllegalArgumentException("Number of cars sold and total value must be non-negative.");
        }

        // Base commission is 2% of the total value of cars sold
        double baseCommission = 0.02 * totalValueSold;

        // Bonus if more than 10 cars sold
        double bonus = (numCarsSold > 10) ? 500 : 0;

        // Extra commission of 1% if total value exceeds $100,000
        double extraCommission = (totalValueSold > 100000) ? 0.01 * totalValueSold : 0;

        // Calculate the total commission
        double totalCommission = baseCommission + bonus + extraCommission;
        return totalCommission;
    }

    public static void main(String[] args) {
        // Example test cases
        testCalculateCommission(5, 50000, 1000.0);
        testCalculateCommission(15, 75000, 2000.0);
        testCalculateCommission(12, 120000, 4100.0);
        testCalculateCommission(0, 0, 0.0);
        testCalculateCommission(-1, 50000, -1); // Expected to handle invalid input
    }

    // Utility method to test the calculateCommission method
    public static void testCalculateCommission(int numCarsSold, double totalValueSold, double expectedCommission) {
        try {
            double result = calculateCommission(numCarsSold, totalValueSold);
            System.out.printf("Cars Sold: %d, Total Value: $%.2f, Expected Commission: $%.2f, Calculated Commission: $%.2f\n",
                    numCarsSold, totalValueSold, expectedCommission, result);
            assert result == expectedCommission : "Test failed!";
        } catch (IllegalArgumentException e) {
            System.out.printf("Invalid Input - Cars Sold: %d, Total Value: $%.2f. Exception: %s\n", numCarsSold, totalValueSold, e.getMessage());
        }
    }
}
