# Kutur ni Jean Admin Dashboard

## Overview

Kutur ni Jean Admin Dashboard is a comprehensive business management system for a Filipino garment rental and custom couture business specializing in abaca (pinukpok-style) designs and premium fabrics. The application provides a complete administrative interface for managing customers, orders, garments, schedules, sales, and fitting appointments.

The system is built as a full-stack web application with a React frontend and Express backend, designed to streamline business operations including rental tracking, custom garment orders, customer management, and financial reporting.

## User Preferences

Preferred communication style: Simple, everyday language.
Technical background: Familiar with React.js, HTML, Bootstrap. Not familiar with TypeScript.
Prefers explanations using familiar React.js concepts rather than TypeScript terminology.

## System Architecture

### Frontend Architecture
- **Framework**: React with TypeScript using Vite as the build tool
- **UI Library**: Shadcn/UI components built on Radix UI primitives
- **Styling**: Tailwind CSS with custom design tokens and CSS variables
- **Routing**: Wouter for client-side routing
- **State Management**: TanStack Query (React Query) for server state management
- **Form Handling**: React Hook Form with Zod validation
- **Theme System**: Custom theme provider supporting light/dark modes

### Backend Architecture
- **Runtime**: Python with Flask framework
- **Language**: Python 3.11 with Flask web framework
- **Database**: PostgreSQL with psycopg2 adapter
- **Database Provider**: Neon Database (serverless PostgreSQL)
- **API Design**: RESTful APIs with JSON responses
- **CORS**: Flask-CORS for React frontend integration

### Database Design
- **Primary Database**: PostgreSQL via Neon Database
- **Schema Management**: Drizzle Kit for migrations and schema management
- **Data Validation**: Zod schemas for runtime type checking
- **Core Entities**: Customers, Garments, Orders, Schedules, Fittings, Feedback, Sales, Users
- **Relationships**: Proper foreign key relationships between entities

### Key Features Architecture
- **Dashboard Analytics**: Real-time business metrics and performance indicators with customizable widgets
- **Customer Management**: Complete customer profiles with order history and preferences
- **Garment Inventory**: Comprehensive catalog with categories, fabrics, and pricing
- **Order Processing**: Rental and custom order lifecycle management
- **Schedule Management**: Appointment booking for fittings, pickups, and returns
- **Sales Reporting**: Financial tracking with visual charts and reports
- **Feedback System**: Customer reviews and ratings for garments
- **Walk-in Fitting**: Manual entry system for non-online customers
- **Settings & Customization**: Drag-and-drop dashboard widgets, localization, notifications, and security settings

### Development Architecture
- **Build System**: Vite for frontend, Python for backend
- **Frontend**: React with TypeScript for type safety and component architecture
- **Backend**: Python Flask with structured API endpoints
- **Code Organization**: Hybrid structure with React frontend and Python Flask backend
- **Development Tools**: Hot module replacement for frontend, Flask debug mode for backend

## External Dependencies

### Database Services
- **Neon Database**: Serverless PostgreSQL database hosting
- **Connection Pooling**: @neondatabase/serverless for optimized database connections

### UI and Styling
- **Radix UI**: Comprehensive primitive component library for accessible UI components
- **Tailwind CSS**: Utility-first CSS framework with custom configuration
- **Lucide React**: Icon library for consistent iconography
- **Recharts**: Chart library for sales and analytics visualizations

### Development and Build Tools
- **Vite**: Frontend build tool with React plugin support
- **Replit Integration**: Development environment plugins for cartographer and runtime error modals
- **PostCSS**: CSS processing with Tailwind and Autoprefixer

### Validation and Forms
- **Zod**: Runtime type validation and schema definition
- **React Hook Form**: Form state management and validation
- **Hookform Resolvers**: Integration between React Hook Form and Zod

### Date and Time
- **date-fns**: Date manipulation and formatting utilities

### Session and Security
- **connect-pg-simple**: PostgreSQL session store for Express sessions
- **WebSocket Support**: ws library for real-time database connections