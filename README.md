# Universal CSV to Supabase Importer

A Python script that automatically imports CSV data into a Supabase database with intelligent data cleaning and validation.

## 🎯 Purpose

This project solves a common problem: **getting CSV data into a structured database quickly and reliably**. Whether you're dealing with product inventories, customer lists, or any other tabular data, this importer handles the messy details of data transformation and database insertion.

## ✨ Features

- **🔒 Secure Credential Management**: Uses environment variables to protect your Supabase API keys
- **🧹 Intelligent Data Cleaning**: Automatically handles missing values, empty strings, and data type conversion
- **🔄 Flexible Column Mapping**: Easily adapt to different CSV formats with simple configuration
- **⚡ Bulk Import**: Efficiently processes large datasets with batch operations
- **🛡️ Error Handling**: Comprehensive error reporting and graceful failure handling
- **📊 Data Validation**: Ensures data integrity before database insertion

## 🏗️ Architecture

```
CSV File → Data Cleaning → Column Mapping → Validation → Supabase Database
```

### Core Components

1. **CSV Reader**: Uses pandas to parse and load CSV data
2. **Data Processor**: Cleans and validates data, handles missing values
3. **Column Mapper**: Translates CSV column names to database schema
4. **Database Client**: Secure connection to Supabase using environment variables
5. **Error Handler**: Comprehensive logging and error reporting

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- A Supabase project with a target table
- Required Python packages (see Installation)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd csv-to-supabase-importer
   ```

2. **Install dependencies**
   ```bash
   pip install pandas supabase python-dotenv
   ```

3. **Set up environment variables**
   - Create a `.env` file in the project root
   - Add your Supabase credentials:
     ```
     SUPABASE_URL="your-supabase-project-url"
     SUPABASE_KEY="your-supabase-anon-key"
     ```

4. **Configure the importer**
   - Update `CSV_FILE_PATH` to point to your CSV file
   - Modify `TABLE_NAME` to match your Supabase table
   - Adjust `column_mapping` to match your CSV structure

### Usage

```bash
python products_csv_importer.py
```

## 📋 Configuration

### Column Mapping

The script uses a flexible column mapping system to handle different CSV formats:

```python
column_mapping = {
    "csv_column_name": "database_column_name",
    "product_id": "product_id",
    "product_name": "product_name",
    "category": "category",
    "price": "price",
    "stock_quantity": "stock_quantity",
    "last_updated": "last_updated",
}
```

### Database Schema

The script expects your Supabase table to have the following structure:

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| `id` | `uuid` | Auto-generated primary key |
| `product_id` | `text` | Unique product identifier |
| `product_name` | `text` | Product name |
| `category` | `text` | Product category |
| `price` | `numeric` | Product price |
| `stock_quantity` | `integer` | Available stock |
| `last_updated` | `text` | Last update date |
| `created_at` | `timestamp` | Auto-generated creation timestamp |

## 🔧 How It Works

### 1. Data Loading
- Reads CSV file using pandas
- Handles various CSV formats and encodings

### 2. Data Cleaning
- Converts all data to strings for consistency
- Replaces `NaN` and empty values with `NULL`
- Validates data against expected schema

### 3. Column Mapping
- Translates CSV column names to database columns
- Filters out unwanted columns
- Ensures data structure matches database schema

### 4. Database Insertion
- Converts data to JSON format for Supabase
- Performs bulk insert operation
- Provides detailed success/error feedback

## 📁 Project Structure

```
csv-to-supabase-importer/
├── products_csv_importer.py    # Main importer script
├── .env                        # Environment variables (not in git)
├── .gitignore                  # Git ignore rules
├── products_database_named.csv # Sample CSV data
└── README.md                   # This file
```

## 🛠️ Customization

### For Different Data Types

To adapt this importer for other types of data:

1. **Update the column mapping** in the script
2. **Modify the database schema** in Supabase
3. **Adjust the CSV file path** configuration
4. **Update validation rules** if needed

### Example: Customer Data

```python
column_mapping = {
    "customer_id": "customer_id",
    "name": "full_name",
    "email": "email_address",
    "phone": "phone_number",
    "city": "location",
}
```

## 🔒 Security Best Practices

- ✅ Never commit `.env` files to version control
- ✅ Use environment variables for all sensitive data
- ✅ Regularly rotate your Supabase API keys
- ✅ Use Row Level Security (RLS) in Supabase for production

## 🐛 Troubleshooting

### Common Issues

**"Supabase credentials not found"**
- Ensure your `.env` file exists and contains valid credentials
- Check that variable names match exactly

**"Column not found in database"**
- Verify your Supabase table schema matches the column mapping
- Ensure all required columns exist in your database

**"Data type mismatch"**
- Check that your CSV data types are compatible with database schema
- Consider adding data type conversion in the script

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🚀 Next Steps

Once your data is in Supabase, you can:

- Build web applications that query this data
- Create APIs using Supabase's auto-generated REST endpoints
- Set up real-time subscriptions for live data updates
- Integrate with other tools and services

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Review the Supabase documentation
3. Open an issue in this repository

---

**Happy importing! 🎉**
