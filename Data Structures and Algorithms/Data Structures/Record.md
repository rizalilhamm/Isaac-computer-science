# Record
A Record is a Data Structure that is consists of a fixed number of variables, called fields. Every field has an identifier (field name) and a data type. Each field in the record can have different data type.

Some language provide his built-in structure such as VB.Net that can used to define a record. In Python we would need to use class or dictionary.


### Example
Suppose you would to creating system for a football club. we can use record to save each information for each team player.
```
PlayerRecord <- RECORD
    player_id: Integer
    first_name: String
    last_name: String
    birth_date: Date
    position: String
    injured: Boolean
ENDRECORD
```

Read more here [Data Structure - Record](https://isaaccomputerscience.org/concepts/dsa_datastruct_record?topic=data_structures)