--
-- PostgreSQL database dump
--

-- Dumped from database version 13.1
-- Dumped by pg_dump version 13.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: parents_tree; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.parents_tree (
    id integer NOT NULL,
    p_id integer,
    name character varying(255)
);


ALTER TABLE public.parents_tree OWNER TO postgres;

--
-- Name: parents_tree_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.parents_tree_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.parents_tree_id_seq OWNER TO postgres;

--
-- Name: parents_tree_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.parents_tree_id_seq OWNED BY public.parents_tree.id;


--
-- Name: parents_tree id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parents_tree ALTER COLUMN id SET DEFAULT nextval('public.parents_tree_id_seq'::regclass);


--
-- Data for Name: parents_tree; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.parents_tree (id, p_id, name) FROM stdin;
1	2	Aleksey
2	3	Aleksandr
3	4	Mykola
4	0	Neznayu
\.


--
-- Name: parents_tree_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.parents_tree_id_seq', 4, true);


--
-- Name: parents_tree parents_tree_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parents_tree
    ADD CONSTRAINT parents_tree_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

