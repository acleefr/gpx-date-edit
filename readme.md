# 🏃 GPX Date Modifier

This Python script allows you to **change only the date** of `<time>` tags in a `.gpx` file, while keeping **the time of day and GPS coordinates** untouched. Perfect for adjusting a GPS track to another day (e.g., for Strava or Garmin).

---

## 🔧 Features

* Keeps original times (`hh:mm:ss`)
* Does not alter coordinates or other metadata
* Cleans up the XML namespace (no `ns0:` tags)
* Generates a clean, ready-to-use `.gpx` file

---

## 📦 How to Use

### 1. Install Python (if not already installed)

Make sure you have Python 3.6+ installed.

### 2. Run the script

```bash
python change_gpx_date.py
```

You can also use it by editing the last lines of the script with the original GPX filename, the output filename, and the new date:

```python
change_gpx_date("bzh.gpx", "1804.gpx", "2025-04-18")
```

---

## 📝 Example

If your original file contains:

```xml
<time>2023-07-22T09:30:00Z</time>
```

And you pass `"2025-04-18"` as the new date, you'll get:

```xml
<time>2025-04-18T09:30:00Z</time>
```

---

## 🧼 Result

The new `.gpx` file will be clean:

* No `ns0:` tags
* Fully compatible with all GPS platforms

---

## 📁 Files

* `change_gpx_date.py` → The Python script
* `README.md` → This documentation file

---

## 🧔 Author

Aclee, Sunday runner
