declare module 'astro:content' {
	interface RenderResult {
		Content: import('astro/runtime/server/index.js').AstroComponentFactory;
		headings: import('astro').MarkdownHeading[];
		remarkPluginFrontmatter: Record<string, any>;
	}
	interface Render {
		'.md': Promise<RenderResult>;
	}

	export interface RenderedContent {
		html: string;
		metadata?: {
			imagePaths: Array<string>;
			[key: string]: unknown;
		};
	}
}

declare module 'astro:content' {
	type Flatten<T> = T extends { [K: string]: infer U } ? U : never;

	export type CollectionKey = keyof AnyEntryMap;
	export type CollectionEntry<C extends CollectionKey> = Flatten<AnyEntryMap[C]>;

	export type ContentCollectionKey = keyof ContentEntryMap;
	export type DataCollectionKey = keyof DataEntryMap;

	type AllValuesOf<T> = T extends any ? T[keyof T] : never;
	type ValidContentEntrySlug<C extends keyof ContentEntryMap> = AllValuesOf<
		ContentEntryMap[C]
	>['slug'];

	/** @deprecated Use `getEntry` instead. */
	export function getEntryBySlug<
		C extends keyof ContentEntryMap,
		E extends ValidContentEntrySlug<C> | (string & {}),
	>(
		collection: C,
		// Note that this has to accept a regular string too, for SSR
		entrySlug: E,
	): E extends ValidContentEntrySlug<C>
		? Promise<CollectionEntry<C>>
		: Promise<CollectionEntry<C> | undefined>;

	/** @deprecated Use `getEntry` instead. */
	export function getDataEntryById<C extends keyof DataEntryMap, E extends keyof DataEntryMap[C]>(
		collection: C,
		entryId: E,
	): Promise<CollectionEntry<C>>;

	export function getCollection<C extends keyof AnyEntryMap, E extends CollectionEntry<C>>(
		collection: C,
		filter?: (entry: CollectionEntry<C>) => entry is E,
	): Promise<E[]>;
	export function getCollection<C extends keyof AnyEntryMap>(
		collection: C,
		filter?: (entry: CollectionEntry<C>) => unknown,
	): Promise<CollectionEntry<C>[]>;

	export function getEntry<
		C extends keyof ContentEntryMap,
		E extends ValidContentEntrySlug<C> | (string & {}),
	>(entry: {
		collection: C;
		slug: E;
	}): E extends ValidContentEntrySlug<C>
		? Promise<CollectionEntry<C>>
		: Promise<CollectionEntry<C> | undefined>;
	export function getEntry<
		C extends keyof DataEntryMap,
		E extends keyof DataEntryMap[C] | (string & {}),
	>(entry: {
		collection: C;
		id: E;
	}): E extends keyof DataEntryMap[C]
		? Promise<DataEntryMap[C][E]>
		: Promise<CollectionEntry<C> | undefined>;
	export function getEntry<
		C extends keyof ContentEntryMap,
		E extends ValidContentEntrySlug<C> | (string & {}),
	>(
		collection: C,
		slug: E,
	): E extends ValidContentEntrySlug<C>
		? Promise<CollectionEntry<C>>
		: Promise<CollectionEntry<C> | undefined>;
	export function getEntry<
		C extends keyof DataEntryMap,
		E extends keyof DataEntryMap[C] | (string & {}),
	>(
		collection: C,
		id: E,
	): E extends keyof DataEntryMap[C]
		? Promise<DataEntryMap[C][E]>
		: Promise<CollectionEntry<C> | undefined>;

	/** Resolve an array of entry references from the same collection */
	export function getEntries<C extends keyof ContentEntryMap>(
		entries: {
			collection: C;
			slug: ValidContentEntrySlug<C>;
		}[],
	): Promise<CollectionEntry<C>[]>;
	export function getEntries<C extends keyof DataEntryMap>(
		entries: {
			collection: C;
			id: keyof DataEntryMap[C];
		}[],
	): Promise<CollectionEntry<C>[]>;

	export function render<C extends keyof AnyEntryMap>(
		entry: AnyEntryMap[C][string],
	): Promise<RenderResult>;

	export function reference<C extends keyof AnyEntryMap>(
		collection: C,
	): import('astro/zod').ZodEffects<
		import('astro/zod').ZodString,
		C extends keyof ContentEntryMap
			? {
					collection: C;
					slug: ValidContentEntrySlug<C>;
				}
			: {
					collection: C;
					id: keyof DataEntryMap[C];
				}
	>;
	// Allow generic `string` to avoid excessive type errors in the config
	// if `dev` is not running to update as you edit.
	// Invalid collection names will be caught at build time.
	export function reference<C extends string>(
		collection: C,
	): import('astro/zod').ZodEffects<import('astro/zod').ZodString, never>;

	type ReturnTypeOrOriginal<T> = T extends (...args: any[]) => infer R ? R : T;
	type InferEntrySchema<C extends keyof AnyEntryMap> = import('astro/zod').infer<
		ReturnTypeOrOriginal<Required<ContentConfig['collections'][C]>['schema']>
	>;

	type ContentEntryMap = {
		"blog": {
"drone-workflow-vietnam-es.md": {
	id: "drone-workflow-vietnam-es.md";
  slug: "drone-workflow-vietnam-es";
  body: string;
  collection: "blog";
  data: any
} & { render(): Render[".md"] };
"drone-workflow-vietnam.md": {
	id: "drone-workflow-vietnam.md";
  slug: "drone-workflow-vietnam";
  body: string;
  collection: "blog";
  data: any
} & { render(): Render[".md"] };
"family-connection-over-composition-es.md": {
	id: "family-connection-over-composition-es.md";
  slug: "family-connection-over-composition-es";
  body: string;
  collection: "blog";
  data: any
} & { render(): Render[".md"] };
"family-connection-over-composition.md": {
	id: "family-connection-over-composition.md";
  slug: "family-connection-over-composition";
  body: string;
  collection: "blog";
  data: any
} & { render(): Render[".md"] };
"guide-to-old-quarter-es.md": {
	id: "guide-to-old-quarter-es.md";
  slug: "guide-to-old-quarter-es";
  body: string;
  collection: "blog";
  data: any
} & { render(): Render[".md"] };
"guide-to-old-quarter.md": {
	id: "guide-to-old-quarter.md";
  slug: "guide-to-old-quarter";
  body: string;
  collection: "blog";
  data: any
} & { render(): Render[".md"] };
"hoi-an-at-dawn-es.md": {
	id: "hoi-an-at-dawn-es.md";
  slug: "hoi-an-at-dawn-es";
  body: string;
  collection: "blog";
  data: any
} & { render(): Render[".md"] };
"hoi-an-at-dawn.md": {
	id: "hoi-an-at-dawn.md";
  slug: "hoi-an-at-dawn";
  body: string;
  collection: "blog";
  data: any
} & { render(): Render[".md"] };
"milky-way-settings-guide-es.md": {
	id: "milky-way-settings-guide-es.md";
  slug: "milky-way-settings-guide-es";
  body: string;
  collection: "blog";
  data: any
} & { render(): Render[".md"] };
"milky-way-settings-guide.md": {
	id: "milky-way-settings-guide.md";
  slug: "milky-way-settings-guide";
  body: string;
  collection: "blog";
  data: any
} & { render(): Render[".md"] };
"quiet-portrait-es.md": {
	id: "quiet-portrait-es.md";
  slug: "quiet-portrait-es";
  body: string;
  collection: "blog";
  data: any
} & { render(): Render[".md"] };
"quiet-portrait.md": {
	id: "quiet-portrait.md";
  slug: "quiet-portrait";
  body: string;
  collection: "blog";
  data: any
} & { render(): Render[".md"] };
"weddings-without-directing-es.md": {
	id: "weddings-without-directing-es.md";
  slug: "weddings-without-directing-es";
  body: string;
  collection: "blog";
  data: any
} & { render(): Render[".md"] };
"weddings-without-directing.md": {
	id: "weddings-without-directing.md";
  slug: "weddings-without-directing";
  body: string;
  collection: "blog";
  data: any
} & { render(): Render[".md"] };
};

	};

	type DataEntryMap = {
		
	};

	type AnyEntryMap = ContentEntryMap & DataEntryMap;

	export type ContentConfig = never;
}
