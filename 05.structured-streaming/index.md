---
Duration: 3 hours
---

# Spark Structured Streaming

## Streaming introduction

- Continuously generated data
- Coming from many data sources simultaneously
- Small in size (kB range)
- Examples: IoT, stock market, recommendation based on geo-location, electricity consumption...
- Unbounded data sets (in opposition to finite data sets)
- Unbounded data processing (in time)
- Spark Structured Streaming: fault-tolerant exactly-once processing

![Streaming](./image/streaming.PNG)

## Difference between batch and stream processing

![Batch vs stream processing](./image/batch_stream_processing.PNG)

## Stream processing models

- Traditional model:

  (-) redundancy
  (+) latency (ms)

![Traditional streaming model](./image/traditional_model.png)

- Micro-batch model:

  (+) redundancy
  (-) latency (100 ms: exactly-once semantics)

![Micro-batch model](./image/microbatch_model.png)

## Different processing semantics

- At-most-once

![At-most-once semantics](./image/at_most_once.png)

- At-least-once

![At-least-once semantics](./image/at_least_once.png)

- Exactly-once

![Exactly-once semantics](./image/exactly_once.png)

[Resource](https://www.splunk.com/en_us/blog/it/exactly-once-is-not-exactly-the-same.html)

## Programming model

Streaming computation as standard batch-like query:

![Streaming programming model](./image/programming_model.png)

Output modes:

- **Complete** - writes all the rows of a result table
- **Append** - writes "new" rows only
- **Update** - writes only the rows that were updated

### Example: Word count

![Streaming programming model: example](./image/example_word_count.png)

## Operations on Streaming DataFrames

The syntax is very similar than what we saw with static DataFrames:

```python
# Streaming DataFrame with IoT device data with schema { device: string, deviceType: string, signal: double, time: DateType}
df = ...

# Select the devices which have signal more than 10
df.select("device").where("signal > 10")

# Running count of the number of updates for each device type
df.groupBy("deviceType").count()
```

SQL-like operations:

```python
df.createOrReplaceTempView("updates")
spark.sql("select count(*) from updates") # returns another streaming DF
```

Several operations are **not supported**: distinct, take(n), limit, chained aggregations, some types of joins...

## Event-time vs. processing time

- **event time** - when the data was generated
- **processing time** - when Spark received the data

![Difference between event time and processing time](./image/event_processing_time.png)

## Windows: tumbling, overlapping

- Each event belongs to one window or more
- Example: Aggregation over a sliding event-time window
  ![Aggregation over a sliding event-time window](./image/sliding_window_aggregation.png)

## Handling late data and how long to wait

![Late events](./image/late_data.png)

### Watermarking

![Watermarking](./image/watermarking.png)

## Vocabulary

- **Event-time** - a time when the event happens
- **Processing time** - a time when we receive the data of the event
- **Trigger** - how often we will collect the data
- **Window** - for how long will we collect the data
- **Watermark** - when the late data is discarded (how late is too late)

---

*The content of this document, including all text, images, and associated materials, is the exclusive property of Adaltas and is protected by applicable copyright laws. Unauthorized distribution, reproduction, or sharing of this content, in whole or in part, is strictly prohibited without the express written consent of the author(s). Any violation of this restriction may result in legal action and the imposition of penalties as prescribed by law.*
