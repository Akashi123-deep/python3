import math
import sys

def calculate_distance(point1: tuple, point2: tuple) -> float:
    try:
        x1, y1, z1 = point1
        x2, y2, z2 = point2
        
        fx1, fy1, fz1 = float(x1), float(y1), float(z1)
        fx2, fy2, fz2 = float(x2), float(y2), float(z2)
        
        return math.sqrt((fx2 - fx1)**2 + (fy2 - fy1)**2 + (fz2 - fz1)**2)
        
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}")
        return 0.0

def main():
    point1 = (10, 20, 5)
    origin = (0, 0, 0)
    
    print("=== Game Coordinate System ===\n")
    print(f"Position created: {point1}")
    dist1 = calculate_distance(point1, origin)
    print(f"Distance between {origin} and {point1}: {dist1:.2f}\n")

    raw_coords = "3,4,0"
    print(f"Parsing coordinates: \"{raw_coords}\"")
    
    parts = raw_coords.split(",")
    parsed_position = tuple(parts) 
    
    dist2 = calculate_distance(parsed_position, origin)
    
    x, y, z = parsed_position
    print(f"Parsed position: ({x}, {y}, {z})")
    print(f"Distance between {origin} and {parsed_position}: {dist2:.1f}\n")

    invalid_raw = "abc,def,ghi"
    print(f"Parsing invalid coordinates: \"{invalid_raw}\"")
    invalid_parts = invalid_raw.split(",")
    invalid_tuple = tuple(invalid_parts)
    
    calculate_distance(invalid_tuple, origin)

    px, py, pz = parsed_position
    print("\nUnpacking demonstration:")
    print(f"Player at x={px}, y={py}, z={pz}")
    print(f"Coordinates: X={px}, Y={py}, Z={pz}")

if __name__ == "__main__":
    main()