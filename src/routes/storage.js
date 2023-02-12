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
		coords: {lat: 40.122138642221444, lng: -74.99880327326689}
	},
]);

/**
 * @type {import('svelte/store').Writable<number>}
 */
export const selectedHouse = writable(-1);