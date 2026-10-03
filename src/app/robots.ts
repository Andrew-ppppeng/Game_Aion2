import type {MetadataRoute} from 'next';
import {site} from '@/lib/site';
export default function robots(): MetadataRoute.Robots {return {rules: process.env.VERCEL_ENV === 'preview' ? {userAgent: '*', disallow: '/'} : {userAgent: '*', allow: '/', disallow: '/api/'}, sitemap: `${site.url}/sitemap.xml`};}
