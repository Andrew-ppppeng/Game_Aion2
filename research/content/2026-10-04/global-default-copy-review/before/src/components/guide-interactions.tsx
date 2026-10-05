'use client';

import dynamic from 'next/dynamic';

// Keep SSR content while loading only the interactions actually rendered by a guide.
export const GuideChecklist = dynamic(() => import('./guide-checklist').then((m) => m.GuideChecklist));
export const GuideFilter = dynamic(() => import('./guide-filter').then((m) => m.GuideFilter));
export const ClassFinder = dynamic(() => import('./class-finder').then((m) => m.ClassFinder));
export const ClassIconTable = dynamic(() => import('./class-finder').then((m) => m.ClassIconTable));
export const EventTimers = dynamic(() => import('./tools/event-timers').then((m) => m.EventTimers));
export const BudgetPlanner = dynamic(() => import('./tools/budget-planner').then((m) => m.BudgetPlanner));
export const MoreEquipment = dynamic(() => import('./tools/more-equipment').then((m) => m.MoreEquipment));
