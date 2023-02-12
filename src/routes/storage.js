import { writable } from 'svelte/store';

export const mapCenter = writable({ lat: 32.7916841, lng: -96.8004513 });

// make a bunch of house objects with these values:
export const houses = writable([
	{
		sqft: 1057,
		listingPrice: 279_000,
		bed: 2,
		bath: 2,
		acres: 1,
		parcelValue: -1,
		description: 'Residential',
		city: 'Dallas',
		coords: {lat: 32.99512755632141, lng: -96.84356606027706}
	},
	{
		sqft: 4000,
		listingPrice: 1_749_000,
		bed: 4,
		bath: 5,
		acres: 0.72,
		parcelValue: -1,
		description: 'Residential',
		city: 'SoCal',
		coords: {lat: 34.24962180644662, lng: -118.46039023140953}
	},
	{
		sqft: 1660,
		listingPrice: 289_900,
		bed: 3,
		bath: 2.5,
		acres: 0.08466483,
		parcelValue: -1,
		description: 'Residential',
		city: 'Philadelphia',
		coords: {lat: 40.055052715822306, lng: -75.14477170241152}
	},
	{
		sqft: 1156,
		listingPrice: 135_000,
		bed: 2,
		bath: 1,
		acres: 0.1890037,
		parcelValue: -1,
		description: 'residential',
		city: 'Dallas',
		coords: {lat: 32.7558625113208, lng: -96.75956357532324}
	},
	{
		sqft: 733,
		listingPrice: 174_900,
		bed: 1,
		bath: 1,
		acres: 2.09,
		parcelValue: -1,
		description: 'residential',
		city: 'Dallas',
		coords: {lat: 32.75581153938154, lng: -96.86061014463658}
	},
	{
		sqft: 1500,
		listingPrice: 246_000,
		bed: 3,
		bath: 2,
		acres: 0.1199954,
		parcelValue: -1,
		description: 'residential',
		city: 'Dallas',
		coords: {lat: 32.77369631658848, lng: -96.74661646028252}
	},
	{
		sqft: 1353,
		listingPrice: 245_000,
		bed: 3,
		bath: 2,
		acres: 0.16799816,
		parcelValue: -1,
		description: 'residential',
		city: 'Dallas',
		coords: {lat: 32.72490131423037, lng: -96.81711894493675}
	},
	{
		sqft: 3492,
		listingPrice: 2_875_000,
		bed: 4,
		bath: 3.5,
		acres: 0.56,
		parcelValue: -1,
		description: 'residential',
		city: 'SoCal',
		coords: {lat: 34.14626458676211, lng: -118.52350340257644}
	},
	{
		sqft: 1574,
		listingPrice: 770_000,
		bed: 4,
		bath: 3,
		acres: 0.04990817,
		parcelValue: -1,
		description: 'residential',
		city: 'SoCal',
		coords: {lat: 34.209292525837554, lng: -118.46342988908222}
	},
	{
		sqft: 1001,
		listingPrice: 575_000,
		bed: 2,
		bath: 2,
		acres: 5.15,
		parcelValue: -1,
		description: 'residential',
		city: 'SoCal',
		coords: {lat: 34.184025106457874, lng: -118.59838410257532}
	},
	{
		sqft: 2464,
		listingPrice: 1_795_000,
		bed: 3,
		bath: 2.5,
		acres: 0.137741,
		parcelValue: -1,
		description: 'residential',
		city: 'SoCal',
		coords: {lat: 34.14368193965825, lng: -118.41236480257645}
	},
	{
		sqft: 1755,
		listingPrice: 395_000,
		bed: 3,
		bath: 2.5,
		acres: 0.08466483,
		parcelValue: -1,
		description: 'residential',
		city: 'Philadelphia',
		coords: {lat: 40.12209035263236, lng: -74.99880131174191}
	},
	{
		sqft: 1728,
		listingPrice: 264_900,
		bed: 4,
		bath: 2.5,
		acres: 0.03599633,
		parcelValue: -1,
		description: 'residential',
		city: 'Philadelphia',
		coords: {lat: 40.034091699430334, lng: -75.03870793124803}
	},
	{
		sqft: 1349,
		listingPrice: 230_000,
		bed: 3,
		bath: 1.5,
		acres: 0.02438017,
		parcelValue: -1,
		description: 'residential',
		city: 'Philadelphia',
		coords: {lat: 40.045500566129085, lng: -75.156819373576}
	},
	{
		sqft: 1495,
		listingPrice: 235_000,
		bed: 4,
		bath: 1.5,
		acres: 0.0312213,
		parcelValue: -1,
		description: 'residential',
		city: 'Philadelphia',
		coords: {lat: 39.97911833686881, lng: -75.25080676008555}
	},
]);

/**
 * @type {import('svelte/store').Writable<number>}
 */
export const selectedHouse = writable(-1);