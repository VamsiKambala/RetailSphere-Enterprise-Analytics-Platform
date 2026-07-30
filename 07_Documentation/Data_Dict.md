# Regions

## Purpose
Stores geographical information used across RetailSphere.

## Owner
Operations Team

## Columns

| Column | Data Type | PK/FK | Description |
|---------|----------|-------|-------------|
| RegionID | INT | PK | Unique region identifier |
| State | VARCHAR | | State name |
| StateCode | VARCHAR | | State abbreviation |
| Zone | VARCHAR | | North, South, East, West, Central |
| GSTRegion | VARCHAR | | GST reporting region |
| Country | VARCHAR | | India |

## Business Rules

- RegionID must be unique.
- One state can appear only once.
- Customers reference RegionID.
- Stores reference RegionID.
- Suppliers reference RegionID.
