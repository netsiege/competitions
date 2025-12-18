<?php
/**
 * Sunspire Energy Heatmap API
 * Backend endpoint for filtering and processing energy data
 * 
 * Uses jq for JSON filtering (fast and efficient)
 */

header('Content-Type: application/json');

$DATA_FILE = __DIR__ . '/data/energy.json';

$action = isset($_GET['action']) ? $_GET['action'] : 'stats';

switch ($action) {
    case 'filter':
        handleFilter();
        break;
    case 'stats':
        handleStats();
        break;
    case 'zones':
        handleZones();
        break;
    default:
        echo json_encode(['error' => 'Unknown action']);
}

/**
 * Filter energy data by region or source
 * Uses jq for efficient JSON processing
 */
function handleFilter() {
    global $DATA_FILE;
    
    $region = isset($_GET['region']) ? $_GET['region'] : null;
    $source = isset($_GET['source']) ? $_GET['source'] : null;
    
    if (!file_exists($DATA_FILE)) {
        echo json_encode(['error' => 'Data file not found']);
        return;
    }
    
    // Build jq filter based on parameters
    if ($region && $source) {
        // Filter by both region and source
        $jq_filter = ".zones[] | select(.region == \"$region\" and .source == \"$source\")";
    } elseif ($region) {
        // Filter by region only
        $jq_filter = ".zones[] | select(.region == \"$region\")";
    } elseif ($source) {
        // Filter by source only  
        $jq_filter = ".zones[] | select(.source == \"$source\")";
    } else {
        // Return all zones
        $jq_filter = ".zones[]";
    }
    
    // Execute jq command to filter data
    $cmd = "jq '$jq_filter' $DATA_FILE";
    $output = shell_exec($cmd);
    
    if ($output === null) {
        echo json_encode(['error' => 'Failed to process data']);
        return;
    }
    
    // Wrap multiple results in array
    $lines = array_filter(explode("\n}\n", trim($output)));
    if (count($lines) > 1) {
        echo '[' . implode(',', array_map('trim', explode("}\n{", $output))) . ']';
    } else {
        echo $output;
    }
}

/**
 * Get overall statistics
 */
function handleStats() {
    global $DATA_FILE;
    
    if (!file_exists($DATA_FILE)) {
        echo json_encode(['error' => 'Data file not found']);
        return;
    }
    
    $cmd = "jq '.' $DATA_FILE";
    $output = shell_exec($cmd);
    echo $output;
}

/**
 * List all available zones
 */
function handleZones() {
    global $DATA_FILE;
    
    if (!file_exists($DATA_FILE)) {
        echo json_encode(['error' => 'Data file not found']);
        return;
    }
    
    $cmd = "jq '.zones[] | {region: .region, name: .name}' $DATA_FILE";
    $output = shell_exec($cmd);
    echo $output;
}
?>
