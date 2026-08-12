# 🤖 Gemini Tool Calling — Fundamentals

A practical Python project designed to understand **LLM Tool Calling** using the **Google Gemini API** and the `google-genai` SDK.

This project starts with a simple calculator tool and gradually introduces multiple tools, tool definitions, tool binding, tool selection, argument extraction, tool execution, and tool results.

The goal is not just to use tool calling, but to understand **how LLMs interact with external Python functions**.

---

## 🚀 Project Goal

The main goal of this project is to understand the complete Tool Calling workflow:

```text
Human Message
      ↓
     LLM
      ↓
Tool Selection
      ↓
AI Tool Call
      ↓
Tool Name + Arguments
      ↓
Tool Registry
      ↓
Tool Executor
      ↓
Python Function
      ↓
Tool Result
      ↓
     LLM
      ↓
Final AI Response