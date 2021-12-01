import java.util.Map;
import java.util.NavigableMap;
import java.util.HashMap;
import java.util.TreeMap;

class TimeMap {

    private Map<String, NavigableMap<Integer, String>> m;

    /** Initialize your data structure here. */
    public TimeMap() {
        m = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        if (!m.containsKey(key))
            m.put(key, new TreeMap<>());
        m.get(key).put(timestamp, value);
    }
    
    public String get(String key, int timestamp) {
        if (!m.containsKey(key))
            return "";
        Map.Entry<Integer, String> entry = m.get(key).floorEntry(timestamp);
        return entry == null ? "" : entry.getValue();
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */
